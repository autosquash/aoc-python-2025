from __future__ import annotations
from src.utils import *


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
