#!/usr/bin/env python3
"""Extract a clean base question sheet from an answered attempt."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ANSWER_BLOCK_RE = re.compile(
    r"\n```(?:markdown)?\n.*?\n```\n\n\*\*Feedback:\*\*\n>.*?\n\n\*\*Marks:\s*[^*]*\*\*",
    re.DOTALL,
)
RESULT_RE = re.compile(r"\n---\n\n## Attempt Result\n\n.*?(?=\n---\n\n#|\Z)", re.DOTALL)


def extract_base(attempt_text: str, title: str | None) -> str:
    text = RESULT_RE.sub("", attempt_text)
    text = ANSWER_BLOCK_RE.sub("", text)
    if title:
        text = re.sub(r"^# .+$", f"# {title}", text, count=1, flags=re.MULTILINE)
    return text.rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a base question sheet from an attempt.")
    parser.add_argument("attempt", type=Path, help="Answered attempt file.")
    parser.add_argument("output", type=Path, help="Base question sheet output path.")
    parser.add_argument("--title", help="Optional replacement title.")
    parser.add_argument("--force", action="store_true", help="Overwrite output if it already exists.")
    args = parser.parse_args()

    if args.output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}. Use --force to replace it.")

    text = args.attempt.read_text(encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(extract_base(text, args.title), encoding="utf-8")


if __name__ == "__main__":
    main()
