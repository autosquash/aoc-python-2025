from __future__ import annotations
import math
from src.utils import *


day_number = get_day_number(__file__)


def solve(lines: list[str]) -> int:
    strings = [[s for s in line.split(" ") if s] for line in lines]
    for s in strings:
        assert "" not in s
    length = len(strings[0])
    assert all(len(s) == length for s in strings)

    *numbers_str, operators = strings
    numbers = [[int(sub) for sub in s] for s in numbers_str]

    total = 0
    for i, op in enumerate(operators):
        problem_numbers = [num[i] for num in numbers]
        if op == "+":
            total += sum(problem_numbers)
        elif op == "*":
            total += math.prod(problem_numbers)

    solution = total
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
