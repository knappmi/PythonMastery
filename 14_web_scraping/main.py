"""Problem 14 — Web scraping with BeautifulSoup

Goal:
  Download https://example.com and extract the page title and all <a> link texts.

Why:
  Teaches HTML parsing, selectors, and robustness (handle missing elements).
"""
from __future__ import annotations
import requests
from bs4 import BeautifulSoup

def scrape_example() -> tuple[str, list[str]]:
    # TODO: return (title, [link_texts...])
    return ("TODO", [])

if __name__ == "__main__":
    print("TODO")
