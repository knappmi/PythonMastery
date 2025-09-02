"""Problem 09 — File I/O

Goal:
  Read a text file line-by-line, uppercase each line, and write to `output.txt` in this folder.

Why:
  Teaches reading/writing files with proper newline handling and context managers.

Run:
  echo -e "hello\nworld" > 09_file_io/input.txt
  python 09_file_io/main.py < 09_file_io/input.txt && cat 09_file_io/output.txt
"""
from __future__ import annotations
import sys, os

def main(argv: list[str]) -> int:
    # TODO: read stdin and write uppercase lines to output.txt next to this script
    with open('09_file_io/output.txt', 'w') as output:
        output.write('')
    with open(argv[0]) as file:
        for line in file:
            upper = line.capitalize()
            with open(f'09_file_io/output.txt', 'a') as output:
                output.write(upper)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
