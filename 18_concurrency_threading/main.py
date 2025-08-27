"""Problem 18 — Concurrency with threading

Goal:
  Start N threads that each perform a simulated task (sleep + compute), collect their results.
  Ensure correct synchronization and join ordering.

Why:
  Teaches Thread, Lock, and shared data coordination.
"""
from __future__ import annotations
import threading, time, random

def worker(i: int, out: list[str], lock: threading.Lock):
    # TODO: sleep random(0.1..0.5), then append a result with locking
    pass

def main(n: int = 5) -> list[str]:
    # TODO: spin up threads, join, return results
    return ["TODO"]

if __name__ == "__main__":
    print(main())
