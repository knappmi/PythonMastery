"""Problem 08 — Context managers

Goal:
  Implement a custom context manager `cd(path)` that temporarily changes the working dir.
  On exit, it must restore the original directory (even if an error occurs).

Why:
  Teaches the context manager protocol and `try/finally` semantics.
"""
from __future__ import annotations
import os
from contextlib import contextmanager

@contextmanager
def cd(path: str):
    # TODO: change into `path` then restore original dir
    yield "TODO"

if __name__ == "__main__":
    print("TODO")
