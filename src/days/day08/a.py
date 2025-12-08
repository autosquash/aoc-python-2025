from __future__ import annotations
import math
from src.utils import *
from typing import Iterator, Sequence


day_number = get_day_number(__file__)

Pos3D = tuple[int, int, int]


def solve(lines: list[str], n: int = 1000) -> int:
    boxes = get_junction_boxes(lines)
    circuits= [{box} for box in boxes]
    ordered = get_nearest_boxes_ordered(boxes)[:n]
    connections = iter([pair for pair, _ in ordered])
    count = 0
    while count < n:
        connection = next(connections)
        process_connection(connection, circuits)
        count += 1

    sizes = sorted([len(c) for c in circuits])

    solution = math.prod(sizes[-3:])
    return solution


def get_junction_boxes(lines: Lines) -> list[Pos3D]:
    boxes: list[Pos3D] = []
    for line in lines:
        pos = tuple([int(s) for s in line.split(",")])
        assert len(pos) == 3
        boxes.append(pos)
    return boxes


def get_nearest_boxes_ordered(
    boxes: Sequence[Pos3D],
) -> list[tuple[tuple[Pos3D, Pos3D], int]]:
    distances: list[tuple[tuple[Pos3D, Pos3D], int]] = []
    n = len(boxes)
    for i in range(n):
        for j in range(i + 1, n):
            if j <= i:
                continue
            a = boxes[i]
            b = boxes[j]
            x, y, z = a
            xx, yy, zz = b
            dist = (x - xx) ** 2 + (y - yy) ** 2 + (z - zz) ** 2
            distances.append(((a, b), dist))
    assert len(distances) == n * (n - 1) / 2, len(distances)
    return sorted(distances, key=lambda tup: tup[1])


def process_connection(
    connection: tuple[Pos3D, Pos3D], circuits: list[set[Pos3D]]
) -> None:
    a, b = connection

    found: list[Pos3D] = []
    for circuit in circuits:
        if a in circuit:
            found.append(a)
        if b in circuit:
            found.append(b)
        if a in circuit and b in circuit:
            break

    assert len(found) == 2
    have_them = [
        i for i, circuit in enumerate(circuits) if a in circuit or b in circuit
    ]

    assert len(have_them) in (1, 2)
    if len(have_them) == 2:
        max_idx = max(have_them)
        min_idx = min(have_them)
        circuits[min_idx] |= circuits[max_idx]
        circuits.remove(circuits[max_idx])


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
