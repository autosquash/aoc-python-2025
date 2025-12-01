import pytest
from typing import Callable, Iterable, TypeVar, cast, Any
from src.utils import *

from . import a, b

given_input = """"""


def test_a() -> None:
    assert given_input, "Missing example input"
    expected = None
    assert expected != None, "Expected is None. Revisar su valor en test_a"
    process(a.solve, expected)


@pytest.mark.skip(reason="Not implemented")
def test_b() -> None:
    assert given_input, "Missing example input"
    expected = None
    assert expected != None, "Expected is None. Revisar su valor en test_b"
    process(b.solve, expected)


@pytest.mark.skip(reason="Not implemented")
def test_func_int() -> None:
    result: int = a.func_int()
    expected = 0
    assert result == expected


@pytest.mark.skip(reason="Not implemented")
def test_func_str() -> None:
    result: str = a.func_str()
    expected = ""
    assert result == expected


T = TypeVar("T", int, str)


def process(solve: Callable[[list[str]], T], expected: T) -> None:
    example = create_example(given_input, expected)
    result = solve(example.lines)
    assert (
        result != 0
    ), "La solución del ejemplo es 0, lo que es improbable. Revisar el retorno del método solve()"
    assert result == example.expected


# def test_examples() -> None:
#     res = a.solve(example.lines)
#     assert res == example.expected


# def test_a() -> None:
#     expected = 0
#     example = create_example(given_input, expected)
#     res = a.solve(example.lines)
#     assert res == example.expected


# def test_b() -> None:
#     expected = 0
#     example = create_example(given_input, expected)
#     res = b.solve(example.lines)
#     assert res == example.expected
