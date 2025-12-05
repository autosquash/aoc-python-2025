from __future__ import annotations
from src.utils import *


day_number = get_day_number(__file__)


def solve(lines: list[str]) -> int:
    ranges: list[str] = []
    for line in lines:
        if line == "":
            break
        ranges.append(line)
    rest = lines[len(ranges) + 1 :]
    numbers = to_int(rest)
    fresh = 0
    for ingredient in numbers:
        for r in ranges:
            start, end = r.split("-")
            if int(start) <= ingredient <= int(end):
                fresh += 1
                break

    solution = fresh
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
