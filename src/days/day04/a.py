from __future__ import annotations
from src.utils import *


day_number = get_day_number(__file__)

Pos = tuple[int, int]


def solve(lines: list[str]) -> int:
    # find rolls with less than 4 roll neighbours
    # empty positions
    empty = get_empty_positions(lines)

    dims = (len(lines[0]), len(lines))

    acc = 0
    for j in range(len(lines)):
        for i in range(len(lines[0])):
            if (i, j) not in empty:
                data = get_neightbours((i, j), dims, empty)
                if data < 4:
                    acc += 1
    solution = acc
    return solution


def get_empty_positions(lines: list[str]) -> set[Pos]:
    empty: set[Pos] = set()
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == ".":
                empty.add((i, j))
    return empty


def get_neightbours(pos: Pos, dims: Pos, grid: set[Pos]) -> int:
    x, y = pos
    neighbours = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    acc = 0
    for x, y in neighbours:
        if 0 <= x < dims[0] and 0 <= y < dims[1]:
            if (x, y) not in grid:
                # it's a roll of paper
                acc += 1

    return acc



def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
