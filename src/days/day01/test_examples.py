from typing import Callable, TypeVar
from src.utils import create_example

from . import a, b

given_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 3
    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 6
    process(b.solve, expected)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert result == example.expected
