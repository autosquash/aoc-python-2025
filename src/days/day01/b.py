from __future__ import annotations
from src.utils import read_data_from_day, print_solution
from .a import day_number

# Part 2


def solve(lines: list[str]) -> int:
    count = 0
    current = 50
    for line in lines:
        direction, *rest = list(line)
        sign = -1 if direction == "L" else 1
        value = int("".join(rest))
        for _ in range(value):
            current += sign
            if current % 100 == 0:
                count += 1

    solution = count
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
