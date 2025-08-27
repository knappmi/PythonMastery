"""Problem 13 — HTTP requests & APIs

Goal:
  Fetch posts from JSONPlaceholder and pretty-print the first 3 titles.
  Endpoint: https://jsonplaceholder.typicode.com/posts

Why:
  Teaches requests, response handling, json(), and errors.
"""
from __future__ import annotations
import requests

def fetch_posts(limit: int = 3) -> list[dict]:
    # TODO: GET and return the first `limit` posts
    return []

def main() -> int:
    # TODO: call fetch_posts and print titles
    print("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
