#!/usr/bin/env python3
"""Aggregate question marks in an attempt and write/update the result block."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


MARK_RE = re.compile(r"\*\*Marks:\s*(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)\*\*", re.IGNORECASE)
RESULT_RE = re.compile(
    r"\n---\n\n## Attempt Result\n\n.*?(?=\n---\n\n#|\Z)",
    re.DOTALL,
)


def format_number(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:.2f}".rstrip("0").rstrip(".")


def result_block(text: str) -> str:
    marks = [(float(score), float(max_score)) for score, max_score in MARK_RE.findall(text)]
    total = sum(score for score, _ in marks)
    possible = sum(max_score for _, max_score in marks)
    answered = len(marks)
    percentage = (total / possible * 100) if possible else 0.0

    return (
        "\n---\n\n"
        "## Attempt Result\n\n"
        f"- Marked questions: {answered}\n"
        f"- Total marks: {format_number(total)}/{format_number(possible)}\n"
        f"- Percentage: {percentage:.1f}%\n"
    )


def update_attempt(text: str) -> str:
    block = result_block(text)
    if RESULT_RE.search(text):
        return RESULT_RE.sub(block, text).rstrip() + "\n"
    return text.rstrip() + block + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate marks and update an attempt result block.")
    parser.add_argument("attempt", type=Path, help="Attempt markdown file to update.")
    parser.add_argument("--check", action="store_true", help="Print the result block without editing the file.")
    args = parser.parse_args()

    text = args.attempt.read_text(encoding="utf-8")
    updated = update_attempt(text)
    if args.check:
        print(result_block(text).strip())
        return
    args.attempt.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
