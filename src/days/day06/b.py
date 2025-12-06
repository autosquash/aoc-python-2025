from __future__ import annotations
import math
from src.utils import *
from .a import day_number

# Part 2


def solve(lines: list[str]) -> int:
    *numbers_lines, operators_line = lines
    starts = [i for i, value in enumerate(operators_line) if value != " "]
    ends = [i - 1 for i in starts[1:]]
    ends.append(len(operators_line))
    operators = [operators_line[i] for i in starts]

    total = 0
    for i, op in enumerate(operators):
        # each column
        start = starts[i]
        end = ends[i]
        column = [num[start:end] for num in numbers_lines]
        problem_size = max(len(num) for num in column)
        assert problem_size == end - start

        # build problem numbers
        problem_numbers: list[int] = []
        for j in range(problem_size):
            in_progress: list[str] = []
            for num in column:
                if len(num) > j:
                    in_progress.append(num[j])
            number_as_str = "".join(in_progress)
            problem_numbers.append(int(number_as_str))

        if op == "+":
            total += sum(problem_numbers)
        if op == "*":
            total += math.prod(problem_numbers)

    solution = total
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
