import pytest
from typing import Callable, Iterable, TypeVar, cast, Any
from src.utils import *

from . import a, b

given_input = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 4277556
    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 3263827
    process(b.solve, expected)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert result == example.expected
