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
    split = line.split(",")
    first = split[0].strip()
    last = split[1].upper()
    email = split[2].strip()
    return f"{last}, {first} {email}"

def main(argv: list[str]) -> int:
    # TODO: read stdin, transform, and print lines
    input = sys.stdin.read().splitlines()
    for line in input:
        print(transform(line))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
