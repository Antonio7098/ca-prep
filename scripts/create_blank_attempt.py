#!/usr/bin/env python3
"""Create a blank attempt file from a base question sheet.

Usage: ca-prep create <base.md>

Auto-detects the attempts/ directory and next attempt number.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


QUESTION_RE = re.compile(r"^(###\s+\d+\.\s+.+)$", re.MULTILINE)


def build_attempt(base_text: str, attempt_num: int) -> str:
    """Convert a base sheet into an answerable attempt document."""

    # Extract title from first line
    title_match = re.search(r"^# (.+)$", base_text, re.MULTILINE)
    base_title = title_match.group(1).strip() if title_match else "Untitled"
    new_title = f"{base_title} - Attempt {attempt_num}"

    # Extract metadata from base sheet
    module_match = re.search(r"- Module: (.+)", base_text)
    module_slug = module_match.group(1).strip() if module_match else ""

    handbook_match = re.search(r"- Handbook: `(.+?)`", base_text)
    handbook_path = handbook_match.group(1) if handbook_match else ""

    today = date.today().strftime("%Y_%m_%d")

    header = f"""# {new_title}

## Attempt Metadata

- Module: {module_slug}
- Sheet: {{{{SHEET_ID}}}}
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
            body_parts.append("")
            body_parts.append("")
            body_parts.append("```")
            body_parts.append("")
            body_parts.append("**Feedback:**")
            body_parts.append("> ")
            body_parts.append("")
            body_parts.append("**Marks: /5**")
            q_count += 1

    return "\n".join(body_parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a blank attempt from a base question sheet."
    )
    parser.add_argument("base", type=Path, help="Path to the base question sheet.")
    parser.add_argument("--force", action="store_true", help="Overwrite the latest attempt if it already exists.")
    args = parser.parse_args()

    if not args.base.exists():
        raise SystemExit(f"Base sheet not found: {args.base}")

    attempts_dir = args.base.parent / "attempts"
    attempts_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(attempts_dir.glob("attempt-*.md"))
    if existing:
        last_num = max(int(f.stem.split("-")[1]) for f in existing if f.stem.count("-") == 1)
        attempt_num = last_num + 1
    else:
        attempt_num = 1

    output = attempts_dir / f"attempt-{attempt_num}.md"

    if output.exists() and not args.force:
        raise SystemExit(
            f"Refusing to overwrite existing file: {output}. "
            f"Use --force to replace it."
        )

    base_text = args.base.read_text(encoding="utf-8")
    output.write_text(build_attempt(base_text, attempt_num), encoding="utf-8")
    print(f"Created: {output}")


if __name__ == "__main__":
    main()
