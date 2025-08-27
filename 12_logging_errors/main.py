"""Problem 12 — Logging & exceptions

Goal:
  Wrap a function that may raise (e.g., division). Log errors with a helpful message and stack trace.

Why:
  Teaches logging config, try/except, and raising custom exceptions.
"""
from __future__ import annotations
import logging, traceback

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

class DivideByZeroError(Exception): ...
def divide(a: float, b: float) -> float:
    # TODO: implement with proper error handling
    return 0.0

def main() -> int:
    # TODO: call divide in a try/except, log errors
    logging.info("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
