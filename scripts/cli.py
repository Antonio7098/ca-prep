#!/usr/bin/env python3
"""Unified CLI for CA exam preparation workflow.

Usage:
  ca-prep create [<path>]                     Create a blank attempt (auto-detects base.md)
  ca-prep extract <attempt.md> <output.md>    Extract base sheet from attempt
  ca-prep finalise <attempt.md>               Finalise an attempt (marks, log, summary)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from scripts.create_blank_attempt import main as create_main
from scripts.extract_base_from_attempt import main as extract_main
from scripts.finalise_attempt import main as finalise_main


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CA exam preparation workflow CLI.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- create ---
    create_p = sub.add_parser("create", help="Create a blank attempt from a base sheet.")
    create_p.add_argument("base", nargs="?", type=Path, default=None, help="Path to the base question sheet or its directory. Defaults to auto-detecting base.md in the current directory.")
    create_p.add_argument("--force", action="store_true", help="Overwrite existing attempt.")

    # --- extract ---
    extract_p = sub.add_parser("extract", help="Extract a base sheet from an answered attempt.")
    extract_p.add_argument("attempt", type=Path, help="Answered attempt file.")
    extract_p.add_argument("output", type=Path, help="Base sheet output path.")
    extract_p.add_argument("--title", help="Optional replacement title.")
    extract_p.add_argument("--force", action="store_true", help="Overwrite output if it exists.")

    # --- finalise ---
    finalise_p = sub.add_parser("finalise", help="Aggregate marks and update attempt result block.")
    finalise_p.add_argument("attempt", type=Path, help="Attempt markdown file to update.")
    finalise_p.add_argument("--check", action="store_true", help="Print result block without editing.")

    args = parser.parse_args()

    if args.command == "create":
        sys.argv = ["create_blank_attempt.py"]
        if args.base is not None:
            sys.argv.append(str(args.base))
        if args.force:
            sys.argv.append("--force")
        create_main()
    elif args.command == "extract":
        sys.argv = ["extract_base_from_attempt.py", str(args.attempt), str(args.output)]
        if args.title:
            sys.argv.extend(["--title", args.title])
        if args.force:
            sys.argv.append("--force")
        extract_main()
    elif args.command == "finalise":
        sys.argv = ["finalise_attempt.py", str(args.attempt)]
        if args.check:
            sys.argv.append("--check")
        finalise_main()


if __name__ == "__main__":
    main()
