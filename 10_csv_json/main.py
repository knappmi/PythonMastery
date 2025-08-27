"""Problem 10 — CSV & JSON

Goal:
  Read a CSV of people (first,last,email), output JSON array of dicts to stdout.

Why:
  Teaches csv module, json dumps, and I/O plumbing.

Run:
  echo -e "first,last,email\nAda,Lovelace,ada@example.com" | python 10_csv_json/main.py
"""
from __future__ import annotations
import sys, csv, json

def main(argv: list[str]) -> int:
    # TODO: read CSV from stdin and print JSON to stdout
    print("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
