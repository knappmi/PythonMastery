"""Problem 03 — String parsing & formatting

Goal:
  Given lines on stdin of the form "first,last,email", output:
    "LAST, FIRST <email>" one per line, last name uppercased.

Why:
  Teaches splitting/joining, validation, formatting, and I/O.

Run:
  echo -e "Ada,Lovelace,ada@example.com\nAlan,Turing,alan@example.org" | python 03_strings_parsing/main.py
  # -> LOVELACE, Ada <ada@example.com>
  # -> TURING, Alan <alan@example.org>
"""
from __future__ import annotations
import sys

def transform(line: str) -> str:
    # TODO: parse and transform a single line
    return "TODO"

def main(argv: list[str]) -> int:
    # TODO: read stdin, transform, and print lines
    print("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
