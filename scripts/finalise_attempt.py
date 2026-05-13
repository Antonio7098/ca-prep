#!/usr/bin/env python3
"""Aggregate question marks in an attempt and write/update the result block."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path


MARK_RE = re.compile(r"\*\*Marks:\s*(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)\*\*", re.IGNORECASE)
CORRECTION_RE = re.compile(r"\*\*Correction:\*\*")
QUESTION_HEADING_RE = re.compile(r"^### (\d+)\.", re.MULTILINE)
BASE_SECTION_RE = re.compile(r"\n---\n")
RESULT_RE = re.compile(
    r"\n---\n\n## Attempt Result\n\n.*?(?=\n---\n\n#|\Z)",
    re.DOTALL,
)
META_RE = re.compile(r"^- (Module|Sheet|Attempt):\s*(.+)$", re.MULTILINE)

OVERVIEW_SECTION_RE = re.compile(
    r"(## Overview\n\n).*?(\n---\n)",
    re.DOTALL,
)
PROGRESS_SECTION_RE = re.compile(
    r"(## Quantitative Progress\n\n).*?(\n---\n)",
    re.DOTALL,
)


def find_base_sheet(attempt_path: Path) -> Path | None:
    base = attempt_path.parent.parent / "base.md"
    return base if base.is_file() else None


def extract_base_answers(base_text: str) -> dict[int, str]:
    answers = {}
    for section in BASE_SECTION_RE.split(base_text):
        qm = QUESTION_HEADING_RE.search(section)
        if not qm:
            continue
        q_num = int(qm.group(1))
        cm = re.search(r"```\n(.*?)\n```", section, re.DOTALL)
        if cm:
            answers[q_num] = cm.group(1).strip()
    return answers


def add_corrections(text: str, base_text: str) -> str:
    answers = extract_base_answers(base_text)
    if not answers:
        return text

    def repl(m: re.Match) -> str:
        before = text[: m.start()]
        qms = list(QUESTION_HEADING_RE.finditer(before))
        if not qms:
            return m.group(0)
        answer = answers.get(int(qms[-1].group(1)))
        if not answer:
            return m.group(0)
        after = text[m.end() : m.end() + 200]
        if CORRECTION_RE.search(after):
            return m.group(0)
        return f"{m.group(0)}\n\n**Correction:**\n```markdown\n{answer}\n```"

    return MARK_RE.sub(repl, text)


def find_project_root(path: Path) -> Path:
    for parent in path.parents:
        if (parent / "README.md").is_file():
            return parent
    import warnings
    warnings.warn("Could not find project root (no README.md in parent chain). Falling back to current directory.")
    return Path.cwd()


def format_number(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:.2f}".rstrip("0").rstrip(".")


def parse_metadata(text: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for m in META_RE.finditer(text):
        meta[m.group(1).lower()] = m.group(2).strip()
    return meta


def scan_attempts(root: Path) -> list[dict]:
    entries: list[dict] = []
    for path in sorted(root.glob("modules/*/questions/*/attempts/*-attempt-*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        marks = [(float(s), float(m)) for s, m in MARK_RE.findall(text)]
        if not marks:
            continue
        total = sum(s for s, _ in marks)
        possible = sum(m for _, m in marks)
        meta = parse_metadata(text)
        sheet = meta.get("sheet", "")
        if not sheet or sheet.startswith("{{"):
            sheet = path.parent.parent.name
        entries.append({
            "sheet": sheet,
            "attempt": meta.get("attempt", ""),
            "total": total,
            "possible": possible,
        })
    return entries


def result_block(text: str) -> tuple[str, dict]:
    marks = [(float(score), float(max_score)) for score, max_score in MARK_RE.findall(text)]
    total = sum(score for score, _ in marks)
    possible = sum(max_score for _, max_score in marks)
    answered = len(marks)
    percentage = (total / possible * 100) if possible else 0.0

    block = (
        "\n---\n\n"
        "## Attempt Result\n\n"
        f"- Marked questions: {answered}\n"
        f"- Total marks: {format_number(total)}/{format_number(possible)}\n"
        f"- Percentage: {percentage:.1f}%\n"
    )

    result_data: dict = {
        "answered": answered,
        "total_marks": f"{format_number(total)}/{format_number(possible)}",
        "total_score": total,
        "possible": possible,
        "percentage": f"{percentage:.1f}",
    }
    return block, result_data


def update_attempt(text: str, base_text: str | None = None) -> tuple[str, dict]:
    if base_text:
        text = add_corrections(text, base_text)
    block, result_data = result_block(text)
    if RESULT_RE.search(text):
        return RESULT_RE.sub(block, text).rstrip() + "\n", result_data
    return text.rstrip() + block + "\n", result_data


def log_to_csv(log_path: Path, attempt_path: Path, text: str, result_data: dict) -> None:
    meta = parse_metadata(text)
    module = meta.get("module", "")
    sheet = meta.get("sheet", "")
    attempt_num = meta.get("attempt", "")

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "module": module,
        "question_sheet": sheet,
        "attempt_number": attempt_num,
        "attempt_file": str(attempt_path),
        "total_marks": result_data["total_marks"],
        "percentage": result_data["percentage"],
        "marked_questions": str(result_data["answered"]),
    }

    file_exists = log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def build_overview(entries: list[dict]) -> str:
    sheets = sorted({e["sheet"] for e in entries if e["sheet"]})
    return (
        "## Overview\n\n"
        f"- **Module in progress:** `01-governance` (AI Governance & Risk Management)\n"
        f"- **Sheets completed:** {len(sheets)} of 12\n"
        f"- **Total attempts:** {len(entries)}\n"
    )


def build_progress_table(entries: list[dict]) -> str:
    lines = [
        "## Quantitative Progress",
        "",
        "| Sheet | Attempt | Score | % |",
        "|---|---|---|---|",
    ]
    total_score = 0.0
    total_possible = 0.0
    for e in entries:
        score = e["total"]
        possible = e["possible"]
        pct = score / possible * 100 if possible else 0
        lines.append(f"| {e['sheet']} | {e['attempt']} | {format_number(score)}/{format_number(possible)} | {pct:.0f}% |")
        total_score += score
        total_possible += possible
    overall_pct = total_score / total_possible * 100 if total_possible else 0
    lines.append(f"| **Cumulative** | | **{format_number(total_score)}/{format_number(total_possible)}** | **{overall_pct:.1f}%** |")
    lines.append("")
    return "\n".join(lines)


def update_learner_summary(root: Path) -> None:
    ls_path = root / "LEARNER_SUMMARY.md"
    if not ls_path.exists():
        return
    text = ls_path.read_text(encoding="utf-8")

    entries = scan_attempts(root)

    overview = build_overview(entries)
    text = OVERVIEW_SECTION_RE.sub(r"\1" + overview[len("## Overview\n\n"):] + r"\2", text)

    progress = build_progress_table(entries)
    text = PROGRESS_SECTION_RE.sub(r"\1" + progress[len("## Quantitative Progress\n\n"):] + r"\2", text)

    ls_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate marks and update an attempt result block.")
    parser.add_argument("attempt", type=Path, help="Attempt markdown file to update.")
    parser.add_argument("--check", action="store_true", help="Print the result block without editing the file.")
    args = parser.parse_args()

    if not args.attempt.is_file():
        raise SystemExit(f"Attempt file not found: {args.attempt}")

    try:
        text = args.attempt.read_text(encoding="utf-8")
    except PermissionError:
        raise SystemExit(f"Permission denied reading: {args.attempt}")
    except UnicodeDecodeError:
        raise SystemExit(f"File is not valid UTF-8: {args.attempt}")

    base_text = None
    base_path = find_base_sheet(args.attempt)
    if base_path:
        base_text = base_path.read_text(encoding="utf-8")

    updated, result_data = update_attempt(text, base_text)
    if args.check:
        print(result_block(text)[0].strip())
        return

    try:
        args.attempt.write_text(updated, encoding="utf-8")
    except PermissionError:
        raise SystemExit(f"Permission denied writing: {args.attempt}")
    except OSError as e:
        raise SystemExit(f"Failed to write {args.attempt}: {e}")

    root = find_project_root(args.attempt)
    log_to_csv(root / "LOG.csv", args.attempt, text, result_data)
    update_learner_summary(root)


if __name__ == "__main__":
    main()
