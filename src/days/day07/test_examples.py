from typing import Callable, TypeVar
from src.utils import *

from . import a, b

given_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = 21
    process(a.solve, expected)


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 40
    process(b.solve, expected)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert (
        result != 0
    ), "La solución del ejemplo es 0, lo que es improbable. Revisar el retorno del método solve()"
    assert result == example.expected
