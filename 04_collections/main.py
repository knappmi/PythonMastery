"""Problem 04 — Collections (lists, dicts, sets)

Goal:
  Given a list of people dicts, produce:
    - A set of unique email domains
    - A dict mapping domain -> count
    - A list of names sorted by last name

Why:
  Teaches core containers, sorting with keys, and dict/set operations.
"""
from __future__ import annotations

PEOPLE = [
    {"first": "Ada", "last": "Lovelace", "email": "ada@example.com"},
    {"first": "Alan", "last": "Turing", "email": "alan@example.org"},
    {"first": "Grace", "last": "Hopper", "email": "grace@navy.mil"},
]

def unique_domains(people: list[dict]) -> set[str]:
    # TODO
    return set()

def domain_counts(people: list[dict]) -> dict[str, int]:
    # TODO
    return {}

def sorted_names(people: list[dict]) -> list[str]:
    # TODO
    return []

if __name__ == "__main__":
    print("TODO")
