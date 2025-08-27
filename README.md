# Python Mastery Problems (20 exercises)

A progressive, hands-on path to Python fluency. Each folder contains a `main.py` with instructions, example I/O, and TODOs.
Run each with a fresh virtual environment. Problems are intentionally small but cover breadth: core syntax, functions, OOP, files,
CLI apps, HTTP, scraping, SQLite, testing, concurrency, and `asyncio`.

## Quick start
```bash
# create & activate venv (Unix/macOS)
python3 -m venv .venv && source .venv/bin/activate

# Windows (PowerShell)
py -m venv .venv; .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
# run a problem
python 01_hello_cli/main.py
```

## Suggested collaboration workflow
1. Fork this repo.
2. Create a branch per problem: `git checkout -b solve/03-strings-mike`.
3. Implement TODOs and run locally.
4. (When tests are present) `pytest`.
5. Open a PR describing your approach and tradeoffs.

## Contents
01. Hello CLI (basics)
02. FizzBuzz variants & logic
03. String parsing & formatting
04. Collections (lists/dicts/sets)
05. Functions & higher-order
06. Comprehensions & generators
07. Decorators
08. Context managers (with)
09. File I/O
10. CSV & JSON
11. argparse CLI
12. Logging & exceptions
13. HTTP requests & APIs
14. Web scraping with BeautifulSoup
15. SQLite CRUD
16. OOP basics (shapes)
17. Unit tests with pytest
18. Concurrency with threading
19. asyncio tasks & gathering
20. Mini Project: TODO CLI app with persistence

## Why this structure?
- **Fluency via repetition**: You see the same ideas from multiple angles.
- **Real-world coverage**: CLI, files, APIs, DB, tests, concurrency.
- **Solo or team**: Each folder is self-contained, ideal for branch-per-problem PRs.
