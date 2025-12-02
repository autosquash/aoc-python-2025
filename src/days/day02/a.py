from __future__ import annotations
import functools
import itertools
from pprint import pprint
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from pathlib import Path
import re
from src.utils import *
from string import ascii_lowercase, ascii_uppercase
from typing import Sequence, Final, NewType


day_number = get_day_number(__file__)


def solve(lines: list[str]) -> int:
    ranges_str = lines[0].split(",")
    acc = 0
    for range_str in ranges_str:
        a, b = range_str.split("-")
        for i in range(int(a), int(b) + 1):
            if is_invalid(i):
                acc += i
    solution = acc
    return solution


def is_invalid(n: int) -> bool:
    """return True if is repeated twice"""
    s = str(n)
    if len(s) % 2 != 0:
        return False

    return s[: len(s) // 2] == s[len(s) // 2 :]


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
