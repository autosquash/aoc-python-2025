from __future__ import annotations
from src.utils import *
from .a import day_number, get_empty_positions, get_neightbours, Pos

# Part 2


def solve(lines: list[str]) -> int:
    # empty positions
    empty = get_empty_positions(lines)

    acc = 0
    while True:
        accesible = get_accesible_rolls((len(lines[0]), len(lines)), empty)
        if not accesible:
            break
        for pos in accesible:
            # pick up roll
            empty.add(pos)
        acc += len(accesible)

    solution = acc
    return solution


def get_accesible_rolls(dims: Pos, grid: set[Pos]) -> list[Pos]:
    accesed: list[Pos] = []
    for j in range(dims[1]):
        for i in range(dims[0]):
            if (i, j)  in grid:
                continue
            data = get_neightbours((i, j), dims, grid)
            if data < 4:
                accesed.append((i, j))
    return accesed


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
