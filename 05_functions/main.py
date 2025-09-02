from __future__ import annotations
from typing import Callable

StrFn = Callable[[str], str]
Pred  = Callable[[str], bool]

def compose(*funcs: StrFn) -> StrFn:
    """
    Return a function that applies the given functions left-to-right.
    compose(f, g, h)("x") == h(g(f("x")))
    If no functions are provided, return the identity function.
    """
    def inner(s: str) -> str:
        for fn in funcs:
            s = fn(s)
        return s
    return inner

def maybe(step: StrFn, predicate: Pred) -> StrFn:
    """
    Return a function that applies `step` only when predicate(s) is True,
    otherwise returns the input unchanged.
    """
    def inner(s: str) -> str:
        return step(s) if predicate(s) else s
    return inner


if __name__ == "__main__":
    pipeline = compose(str.strip, str.lower, str.title)
    print(pipeline("   hello WORLD  "))  # -> "Hello World"

    # Conditional step: capitalize only if the string looks "shouty"
    is_shouty = lambda s: any(c.isalpha() for c in s) and s == s.upper()
    pipeline2 = compose(str.strip, maybe(str.title, is_shouty))
    print(pipeline2("   HELLO WORLD  "))  # -> "Hello World"
    print(pipeline2("   hello world  "))  # -> "hello world"
