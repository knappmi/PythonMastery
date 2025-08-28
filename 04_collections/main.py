"""Problem 04 — Collections (lists, dicts, sets)

Goal:
  Given a list of people dicts, produce:
    - A set of unique email domains
    - A dict mapping domain -> count
    - A list of names sorted by last name

Why:
  Teaches core containers, sorting with keys, and dict/set operations.
"""
from __future__ import annotations

from collections import defaultdict

PEOPLE = [
    {"first": "Ada", "last": "Lovelace", "email": "ada@example.com"},
    {"first": "Alan", "last": "Turing", "email": "alan@example.org"},
    {"first": "Grace", "last": "Hopper", "email": "grace@navy.mil"},
    {"first": "Bob", "last": "Greene", "email": "bob@example.com"},
    {"first": "Charlie", "last": "Bucket", "email": "charlie@navy.mil"}
]

def unique_domains(people: list[dict]) -> set[str]:
    domains = []
    for person in people:
        if person["email"]:
            split_email = person["email"].split("@")
            domains.append(split_email[1])
    return set(domains)

def domain_counts(people: list[dict]) -> dict[str, int]:
    domain_dict = {}
    for person in people:
        if person["email"]:
            split_email = person["email"].split("@")
            if split_email[1] in domain_dict.keys():
                email_count = domain_dict.get(split_email[1])
                domain_dict[split_email[1]] = email_count + 1
            else:
                domain_dict.update({split_email[1]: 1})
        else:
            print(f"{domain_dict[person["first"]]} doesn't have an email address")
            continue
    return domain_dict

def sorted_names(people: list[dict]) -> list[str]:
    names = []
    for person in people:
        names.append(person["last"] + ", " + person["first"])

    return sorted(names)

if __name__ == "__main__":
    print(unique_domains(PEOPLE))
    print(domain_counts(PEOPLE))
    print(sorted_names(PEOPLE))
