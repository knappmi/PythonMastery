"""Problem 11 — argparse CLI

Goal:
  Build a CLI `greet`:
    python 11_argparse_cli/main.py --name Mike --shout
  It prints "Hello, Mike!" or SHOUTS if --shout is set.

Why:
  Teaches argparse options, defaults, and flags.
"""
from __future__ import annotations
import sys, argparse

def build_parser() -> argparse.ArgumentParser:
    # TODO: define --name and --shout
    return argparse.ArgumentParser()

def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
