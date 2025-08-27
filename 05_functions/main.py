"""Problem 05 — Functions & higher-order

Goal:
  Implement a tiny pipeline framework where you can compose simple transforms:
    pipeline = compose(strip, lower, title)
    result = pipeline("   hello WORLD  ")
  Add an optional `predicate` to conditionally apply a step.

Why:
  Teaches function defs, callables, closures, and composition.
"""
from __future__ import annotations
from typing import Callable, Iterable

def compose(*funcs: Callable[[str], str]) -> Callable[[str], str]:
    # TODO: return a function that applies funcs left-to-right
    def inner(s: str) -> str:
        return "TODO"
    return inner

def maybe(step: Callable[[str], str], predicate: Callable[[str], bool]) -> Callable[[str], str]:
    # TODO: only apply step if predicate(s) is True
    def inner(s: str) -> str:
        return "TODO"
    return inner

if __name__ == "__main__":
    print("TODO")
