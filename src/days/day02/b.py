from __future__ import annotations
from src.utils import *
from .a import day_number

# Part 2


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
    """return True if is repeated m times"""
    s = str(n)

    for factor in range(2, len(s) + 1):
        if is_repeated_m_times(s, factor):
            return True
    return False


def is_repeated_m_times(s: str, factor: int) -> bool:
    if len(s) % factor != 0:
        return False
    chunk = len(s) // factor
    for i in range(factor - 1):
        start = i * chunk
        middle = start + chunk
        end = middle + chunk
        if s[start:middle] != s[middle:end]:
            return False
    return True


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
