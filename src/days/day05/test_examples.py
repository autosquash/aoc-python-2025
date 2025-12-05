from typing import Callable, TypeVar
from src.days.day05 import b
from src.utils import *

from . import a, b

given_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

given_input_01 = """3-5
10-14
16-20
12-18
20-24
"""


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 3
    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 14
    process(b.solve, expected)


def test_b_01() -> None:
    assert given_input_01, "Missing example input"
    expected = 18
    example = create_example(given_input_01, expected)
    result = b.solve(example.lines)
    assert result == example.expected


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert result == example.expected
