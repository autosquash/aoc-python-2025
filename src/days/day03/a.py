from __future__ import annotations
from src.utils import *


day_number = get_day_number(__file__)


def solve(lines: list[str]) -> int:
    acc = 0
    for _, line in enumerate(lines):
        numbers = [int(s) for s in line]
        max_first = max(numbers[:-1])
        first_idx = 0
        for j, n in enumerate(numbers[:-1]):
            if n == max_first:
                first_idx = j
                break
        length = len(numbers)
        second = max(numbers[j] for j in range(first_idx + 1, length))
        joltage = max_first * 10 + second
        acc += joltage

    solution = acc
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
