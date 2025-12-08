from typing import Callable, TypeVar
from src.utils import *

from . import a, b

given_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def test_a() -> None:
    expected = 40
    example = create_example(given_input, expected)
    res = a.solve(example.lines, 10)
    assert res == example.expected


def test_b() -> None:
    assert given_input, "Missing example input"
    expected = 25272
    process(b.solve, expected)


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert (
        result != 0
    ), "La solución del ejemplo es 0, lo que es improbable. Revisar el retorno del método solve()"
    assert result == example.expected
