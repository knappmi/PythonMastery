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
    return [i ** 2 for i in range(1, n + 1) if i % 2 == 0]

def fib(limit: int):
    # TODO: generator yielding Fibonacci numbers <= limit
    def _fib() -> int:
        a, b = 0, 1
        for _ in range(limit):
            yield a
            a, b = b, a + b
    yield from _fib()

from typing import Iterable, Generator

def long_words(words: Iterable[str], k: int) -> Generator[str, None, None]:
    def count_letters(word_list: Iterable[str], k: int):
        for word in word_list:
            if len(word) >= k:
                yield word

    yield from count_letters(words, k)


if __name__ == "__main__":
    for x in fib(50):
        print(x, end=" ")

    print(squares_of_evens(20))

    print(list(long_words(["hello", "hi", "world", "go"], 5)))
