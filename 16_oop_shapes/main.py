"""Problem 16 — OOP basics (shapes)

Goal:
  Define classes `Circle` and `Rectangle` with area/perimeter methods.
  Add `__repr__` and type hints; validate inputs.

Why:
  Teaches classes, methods, dataclasses (optional), and dunder methods.
"""
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    # TODO: area(), perimeter()

@dataclass
class Rectangle:
    width: float
    height: float
    # TODO: area(), perimeter()

if __name__ == "__main__":
    print("TODO")
