"""Problem 06 — Comprehensions & generators

Goal:
  Build:
    1) a list comprehension that squares even numbers from 1..N
    2) a generator that yields Fibonacci numbers up to a limit
    3) a generator expression that filters words longer than k

Why:
  Teaches concise data pipelines and lazy iteration.
"""
from __future__ import annotations
from typing import Iterable

def squares_of_evens(n: int) -> list[int]:
    # TODO
    return []

def fib(limit: int):
    # TODO: generator yielding Fibonacci numbers <= limit
    yield from ()

def long_words(words: Iterable[str], k: int):
    # TODO: generator expression or function yielding long words
    yield from ()

if __name__ == "__main__":
    print("TODO")
