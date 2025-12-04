from typing import Callable, TypeVar
from src.utils import *

from . import a, b

given_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 357

    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 3121910778619
    process(b.solve, expected)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert (
        result != 0
    ), "La solución del ejemplo es 0, lo que es improbable. Revisar el retorno del método solve()"
    assert result == example.expected
