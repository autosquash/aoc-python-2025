from __future__ import annotations
from src.utils import *
from .a import day_number

# Part 2


def solve(lines: list[str]) -> int:
    ranges: list[str] = []
    for i, line in enumerate(lines):
        if line == "":
            break
        ranges.append(line)

    fresh_ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

    while True:
        changed = False
        unique: list[tuple[int, int]] = []
        for r in fresh_ranges:
            start, end = r
            for i, prev in enumerate(unique):
                prev_start, prev_end = prev

                if start > prev_end or end < prev_start:
                    # not collide
                    continue

                # collide
                new_start = prev_start if start > prev_start else start
                new_end = prev_end if end < prev_end else end
                unique[i] = (new_start, new_end)
                changed = True
                break
            else:
                unique.append(r)

        if not changed:
            assert unique == fresh_ranges
            break
        else:
            fresh_ranges = unique
    acc = 0
    for start, end in unique:
        acc += (end - start) + 1

    solution = acc
    return solution


def main() -> None:
    print("Part 2")
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
