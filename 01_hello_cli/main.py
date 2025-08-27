"""Problem 01 — Hello CLI (basics)

Goal:
  Print "Hello, <name>!" to stdout. If a name is provided as the first CLI arg, use it;
  otherwise default to "World".

Why:
  Teaches running scripts, sys.argv, basic branching, and f-strings.

Run:
  python 01_hello_cli/main.py Mike
  # -> Hello, Mike!

TODOs:
  1) Read optional name from sys.argv.
  2) Default to "World" if no name provided.
  3) Print the greeting.
"""
from __future__ import annotations
import sys

def main(argv: list[str]) -> int:
    # TODO: implement
    if len(argv) == 0:
        return "Hello, World!"
    else:
        return print(f'Hello, {argv[0]}!')

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
