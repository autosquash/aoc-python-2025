from __future__ import annotations
from collections import defaultdict, deque
from src.utils import *
from .a import day_number

# Part 2


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
    q: deque[Pos] = deque([start])
    visited: set[Pos] = set()
    universes: dict[Pos, int] = defaultdict(int)
    universes[start] = 1
    while q:
        current = q.popleft()
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        if y + 1 == dims[1]:
            continue
        times = universes[current]
        down = (x, y + 1)
        if down not in world:
            q.append(down)
            universes[down] += times
            continue

        assert world[down] == "^", world[down]
        x, y = down
        left = (x - 1, y)
        right = (x + 1, y)
        for new in (left, right):
            q.append(new)
            universes[new] += times

    last_row = max(y for _, y in universes)

    count = 0
    for (x, y), times in universes.items():
        if y == last_row:
            count += times

    solution = count
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
