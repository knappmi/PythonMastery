"""Problem 20 — Mini Project: TODO CLI app with persistence

Goal:
  Build a CLI to manage TODOs stored in a JSON file in this folder:
    - add <text>
    - list
    - done <id>
    - delete <id>

Why:
  Pulls together argparse, files, JSON, and clean code structure.

Run:
  python 20_project_todo_cli/main.py add "Buy milk"
  python 20_project_todo_cli/main.py list
"""
from __future__ import annotations
import sys, argparse, json, os
from dataclasses import dataclass, asdict
from typing import Any

DATA_PATH = os.path.join(os.path.dirname(__file__), "todos.json")

def load() -> list[dict]:
    # TODO: read JSON if exists, else return []
    return []

def save(items: list[dict]) -> None:
    # TODO: write JSON atomically
    pass

def cmd_add(text: str) -> None:
    # TODO
    pass

def cmd_list() -> None:
    # TODO
    pass

def cmd_done(i: int) -> None:
    # TODO
    pass

def cmd_delete(i: int) -> None:
    # TODO
    pass

def build_parser() -> argparse.ArgumentParser:
    # TODO: subcommands add/list/done/delete
    return argparse.ArgumentParser()

def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print("TODO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
