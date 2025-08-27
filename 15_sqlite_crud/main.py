"""Problem 15 — SQLite CRUD

Goal:
  Create a SQLite DB file `people.db` with a `people` table (id, first, last, email).
  Implement basic CRUD and print all rows.

Why:
  Teaches sqlite3, parameterized queries, and context managers.
"""
from __future__ import annotations
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(__file__), "people.db")

def init_db():
    # TODO: create table if not exists
    pass

def add_person(first: str, last: str, email: str) -> int:
    # TODO: insert and return new id
    return -1

def list_people() -> list[tuple]:
    # TODO: return all rows
    return []

if __name__ == "__main__":
    print("TODO")
