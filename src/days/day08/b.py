from __future__ import annotations
import math
from src.utils import *
from .a import (
    day_number,
    get_junction_boxes,
    get_nearest_boxes_ordered,
    Pos3D,
    process_connection,
)

# Part 2


def solve(lines: list[str]) -> int:
    boxes = get_junction_boxes(lines)
    circuits= [{box} for box in boxes]
    ordered = get_nearest_boxes_ordered(boxes)
    connections = iter([pair for pair, _ in ordered])
    connection: tuple[Pos3D, Pos3D] | None = None
    while len(circuits) > 1:
        connection = next(connections)
        process_connection(connection, circuits)

    assert connection
    solution = math.prod(pos[0] for pos in connection)
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
