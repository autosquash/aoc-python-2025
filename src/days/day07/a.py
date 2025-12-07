from __future__ import annotations
from pprint import pprint
from collections import deque
from src.utils import *


day_number = get_day_number(__file__)


Pos = tuple[int, int]


def solve(lines: list[str]) -> int:
    world: dict[Pos, str] = {}
    start: Pos | None = None
    x: int | None = None
    y: int | None = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                world[(x, y)] = char
                if char == "S":
                    start = (x, y)
    assert start
    assert x
    assert y
    dims = (x + 1, y + 1)
    q = deque([start])
    visited: set[Pos] = set()
    split_count = 0
    while q:
        current = q.popleft()
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        if y + 1 == dims[1]:
            continue
        down = (x, y + 1)
        if down not in world:
            q.append(down)
            continue

        assert world[down] == "^", world[down]
        x, y = down
        q.append((x - 1, y))
        q.append((x + 1, y))
        split_count += 1

    solution = split_count
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
