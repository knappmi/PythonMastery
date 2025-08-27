"""Problem 17 — Unit tests with pytest

Goal:
  Implement `slugify(text)` that:
    - lowercases
    - replaces non-alphanumerics with hyphens
    - collapses multiple hyphens
    - strips leading/trailing hyphens

Why:
  Teaches TDD, pytest assertions, and edge cases.
"""
from __future__ import annotations
import re

def slugify(text: str) -> str:
    # TODO: implement
    return "TODO"

# ----------------- Tests -----------------
def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"

def test_slugify_multiple_spaces_and_symbols():
    assert slugify("Hello  ---  World!!!") == "hello-world"

def test_slugify_unicode():
    assert slugify("Café du Monde") == "caf-du-monde"  # naive ASCII-only for now

def test_slugify_edges():
    assert slugify("  --Already--sluggy-- ") == "already-sluggy"
