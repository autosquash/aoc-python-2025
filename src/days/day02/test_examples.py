import pytest
from typing import Callable, Iterable, TypeVar, cast, Any
from src.utils import *

from . import a, b

given_input = "".join(
    """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124""".splitlines()
)


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 1227775554
    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 4174379265
    process(b.solve, expected)


def test_func_int() -> None:
    assert b.is_invalid(2323)
    assert b.is_invalid(232323)
    assert b.is_invalid(234234234)
    assert not b.is_invalid(2323232)
    assert not b.is_invalid(2)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert result == example.expected
