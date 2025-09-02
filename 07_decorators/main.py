"""Problem 07 — Decorators

Goal:
  Write a decorator `timeit` that measures runtime of a function and prints it.
  Then decorate a slow function (e.g., sleep).

Why:
  Teaches first-class functions, closures, functools.wraps.
"""
from __future__ import annotations
import time
from functools import wraps

def timeit(func):
    # TODO: implement decorator that prints runtime
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start} seconds")
        return value
    return wrapper

if __name__ == "__main__":
    @timeit
    def slow_func(t):
        time.sleep(t)
        return print(f"Slow function complete")

    slow_func(1)
