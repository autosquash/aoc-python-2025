from __future__ import annotations
from src.utils import *
from .a import day_number

# Part 2


def solve(lines: list[str]) -> int:
    acc = 0
    for _, line in enumerate(lines):
        numbers = [int(s) for s in line]
        joltage = calculate(numbers)
        acc += joltage

    solution = acc
    return solution


def calculate(numbers: list[int]) -> int:
    in_process: list[int] = []
    length = len(numbers)
    first_idx = 0
    while len(in_process) < 12:
        missing = 12 - len(in_process)
        last_idx = length - missing
        n = max(numbers[first_idx : last_idx + 1])
        for i in range(first_idx, last_idx + 1):
            if numbers[i] == n:
                first_idx = i + 1
                break
        in_process.append(n)
    strs = [str(n) for n in in_process]
    assert len(strs) == 12
    s = "".join(strs)
    return int(s)


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
