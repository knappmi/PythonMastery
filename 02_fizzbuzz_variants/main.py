"""Problem 02 — FizzBuzz variants & logic

Goal:
  Print numbers 1..100 with rules:
    - Multiples of 3 => "Fizz"
    - Multiples of 5 => "Buzz"
    - Multiples of both => "FizzBuzz"
  Variant: Accept custom ranges and divisors via args.
  
Why:
  Teaches loops, conditionals, modular arithmetic, and simple CLI parsing.

Run:
  python 02_fizzbuzz_variants/main.py
  python 02_fizzbuzz_variants/main.py 1 50 2 7
"""
from __future__ import annotations
import sys

def fizzbuzz(start: int, end: int, a: int = 3, b: int = 5) -> list[str]:
    # TODO: implement core logic and return list of strings
    for i in range(start, end):
        word = ""
        print(f"{i}...")
        if i % a == 0:
            word += "Fizz"
        if i % b == 0:
            word += "Buzz"
        if word == "":
            print(f"{i} is not a multiple of {a} or {b}.")
        else:
            print(word)
    return 0

def main(argv: list[str]) -> int:
    # TODO: parse optional args and print results
    return fizzbuzz(*map(int, argv))

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
