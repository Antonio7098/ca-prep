#!/usr/bin/env python3
"""Create a blank attempt file from a base question sheet.

Usage:
  ca-prep create                          # auto-detect base.md in current dir
  ca-prep create <path>                   # path to base.md or its directory

Auto-detects the attempts/ directory and next attempt number.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


QUESTION_RE = re.compile(r"^(###\s+\d+\.\s+.+)$", re.MULTILINE)
MARKS_RE = re.compile(r"\*\*Marks: /(\d+)\*\*|\*\*Total Marks: (\d+)\*\*")


def extract_question_marks(base_text: str) -> list[int]:
    return [
        int((m.group(1) or m.group(2)))
        for m in MARKS_RE.finditer(base_text)
    ]


def build_attempt(base_text: str, attempt_num: int) -> str:
    """Convert a base sheet into an answerable attempt document."""

    # Extract title from first line
    title_match = re.search(r"^# (.+)$", base_text, re.MULTILINE)
    base_title = title_match.group(1).strip() if title_match else "Untitled"
    new_title = f"{base_title} - Attempt {attempt_num}"

    # Extract metadata from base sheet
    module_match = re.search(r"- Module: (.+)", base_text)
    module_slug = module_match.group(1).strip() if module_match else ""

    area_match = re.search(r"- Area: (.+)", base_text)
    area_slug = area_match.group(1).strip() if area_match else "unknown"

    handbook_match = re.search(r"- Handbook: `(.+?)`", base_text)
    handbook_path = handbook_match.group(1) if handbook_match else ""

    today = date.today().strftime("%Y_%m_%d")

    header = f"""# {new_title}

## Attempt Metadata

- Module: {module_slug}
- Sheet: {area_slug}
- Attempt: {attempt_num}
- Date: {today}
- Handbook: `{handbook_path}`

---
"""

    # Extract section headers and questions from base
    struct_re = re.compile(
        r"^(# SECTION \d.+)$|^(## (?!Sheet Metadata).+)$|^(### \d+\..+)$",
        re.MULTILINE,
    )

    max_marks_list = extract_question_marks(base_text)

    body_parts = [header]
    q_count = 0
    for match in struct_re.finditer(base_text):
        if match.group(1):  # section heading
            body_parts.append("")
            body_parts.append(match.group(1))
        elif match.group(2):  # subsection heading
            body_parts.append("")
            body_parts.append(match.group(2))
        elif match.group(3):  # question
            if q_count > 0:
                body_parts.append("")
                body_parts.append("---")
            body_parts.append("")
            body_parts.append(match.group(3))
            body_parts.append("")
            body_parts.append("```markdown")
            body_parts.append("")
            body_parts.append("```")
            body_parts.append("")
            max_m = max_marks_list[q_count] if q_count < len(max_marks_list) else 5
            body_parts.append(f"**Total Marks: {max_m}**")
            q_count += 1

    return "\n".join(body_parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a blank attempt from a base question sheet."
    )
    parser.add_argument("base", nargs="?", type=Path, default=None, help="Path to the base question sheet or its directory. Defaults to auto-detecting base.md in the current directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite the latest attempt if it already exists.")
    args = parser.parse_args()

    if args.base is None:
        candidates = [Path.cwd() / "base.md"]
    elif args.base.is_dir():
        candidates = [args.base / "base.md"]
    else:
        candidates = [args.base]

    base_path = next((p for p in candidates if p.is_file()), None)
    if base_path is None:
        sources = "\n".join(f"  {p}" for p in candidates)
        raise SystemExit(
            f"Base sheet not found. Tried:\n{sources}"
        )

    sheet_dir_name = base_path.parent.name
    attempts_dir = base_path.parent / "attempts"
    attempts_dir.mkdir(parents=True, exist_ok=True)

    prefix = f"{sheet_dir_name}-attempt-"
    existing = sorted(attempts_dir.glob(f"{prefix}*.md"))
    if existing:
        nums = []
        for f in existing:
            try:
                num = int(f.stem.split("-")[-1])
                nums.append(num)
            except (ValueError, IndexError):
                continue
        attempt_num = max(nums) + 1 if nums else 1
    else:
        attempt_num = 1

    output = attempts_dir / f"{prefix}{attempt_num}.md"

    if output.exists() and not args.force:
        raise SystemExit(
            f"Refusing to overwrite existing file: {output}. "
            f"Use --force to replace it."
        )

    try:
        base_text = base_path.read_text(encoding="utf-8")
    except PermissionError:
        raise SystemExit(f"Permission denied reading: {base_path}")
    except UnicodeDecodeError:
        raise SystemExit(f"File is not valid UTF-8: {base_path}")

    try:
        output.write_text(build_attempt(base_text, attempt_num), encoding="utf-8")
    except PermissionError:
        raise SystemExit(f"Permission denied writing: {output}")
    except OSError as e:
        raise SystemExit(f"Failed to write {output}: {e}")

    print(f"Created: {output}")


if __name__ == "__main__":
    main()
