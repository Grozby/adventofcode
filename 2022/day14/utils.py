from typing import List, Tuple

import numpy as np


def parse_input() -> Tuple[List[List[List[int]]], Tuple[int, int, int]]:
    rock_structures = []

    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            rock_structures.append(
                [[int(xt) for xt in x.split(",")] for x in line.split(" -> ")])

    x_max, y_max = 0, 0
    x_min = float("inf")
    for rs in rock_structures:
        for (x, y) in rs:
            x_max = max(x, x_max)
            x_min = min(x, x_min)
            y_max = max(y, y_max)

    return rock_structures, (x_max, x_min, y_max)


def populate_map(scan_map: np.ndarray, rock_structures: List[List[List[int]]]):
    for rock_structure in rock_structures:
        for (x1, y1), (x2, y2) in zip(rock_structure[:-1], rock_structure[1:]):
            if x1 == x2:
                mi, ma = sorted([y1, y2])
                scan_map[mi:ma + 1, x1] = 1
            else:
                mi, ma = sorted([x1, x2])
                scan_map[y1, mi:ma + 1] = 1
    return scan_map
