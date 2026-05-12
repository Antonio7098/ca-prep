#!/usr/bin/env python3
"""Create a blank attempt file from a base question sheet."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


QUESTION_RE = re.compile(r"^(###\s+\d+\.\s+.+)$", re.MULTILINE)


def build_attempt(base_text: str, title: str | None) -> str:
    """Convert a base sheet into an answerable attempt document."""
    if title:
        base_text = re.sub(r"^# .+$", f"# {title}", base_text, count=1, flags=re.MULTILINE)

    def add_answer_block(match: re.Match[str]) -> str:
        return (
            f"{match.group(1)}\n\n"
            "```markdown\n\n\n\n```\n\n"
            "**Feedback:**\n> \n\n"
            "**Marks: /5**"
        )

    text = QUESTION_RE.sub(add_answer_block, base_text)
    return text.rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a blank attempt from a base question sheet.")
    parser.add_argument("base", type=Path, help="Path to the base question sheet.")
    parser.add_argument("output", type=Path, help="Path to write the blank attempt.")
    parser.add_argument("--title", help="Optional title for the generated attempt.")
    parser.add_argument("--force", action="store_true", help="Overwrite output if it already exists.")
    args = parser.parse_args()

    if args.output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}. Use --force to replace it.")

    base_text = args.base.read_text(encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_attempt(base_text, args.title), encoding="utf-8")


if __name__ == "__main__":
    main()
