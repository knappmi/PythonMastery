"""Problem 19 — asyncio tasks & gathering

Goal:
  Launch several async tasks (e.g., fake fetches) and gather results.
  Add a timeout; handle cancellations cleanly.

Why:
  Teaches asyncio.run, create_task, gather, and cancellation.
"""
from __future__ import annotations
import asyncio, random

async def fetch(i: int) -> str:
    # TODO: await sleep for a random time, return a result string
    return "TODO"

async def main_async(n: int = 5) -> list[str]:
    # TODO: create tasks, gather with timeout
    return ["TODO"]

if __name__ == "__main__":
    print(asyncio.run(main_async()))
