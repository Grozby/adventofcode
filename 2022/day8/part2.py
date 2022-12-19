import itertools

import numpy as np


def _in_bounds(x: int, min_x: int = 0, max_x: int = 1) -> bool:
    return (x >= min_x) and (x < max_x)


def in_bounds(tree_map: np.ndarray, pos: np.ndarray) -> bool:
    return (_in_bounds(pos[0], max_x=len(tree_map)) and _in_bounds(
        pos[1], max_x=len(tree_map[0])))


def in_bounds_and_higher(tree_map: np.ndarray, ref_pos: np.ndarray,
                         pos: np.ndarray,) -> bool:
    return (in_bounds(tree_map=tree_map, pos=pos) and
            tree_map[pos[0], pos[1]] < tree_map[ref_pos[0], ref_pos[1]])


def get_scenic_score(tree_map: np.ndarray, position: np.ndarray) -> int:
    scenic_score = 1

    increments = np.array([
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ])

    for inc in increments:
        cp = position.copy() + inc
        while in_bounds_and_higher(tree_map, position, cp):
            cp += inc

        n_trees_seeing = np.abs(np.sum(position - cp))
        if not in_bounds(tree_map, cp):
            n_trees_seeing -= 1
        scenic_score *= max(n_trees_seeing, 1)

    return scenic_score


if __name__ == "__main__":
    tree_map = []
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            tree_map.append([int(x) for x in list(line)])
    tree_map = np.array(tree_map)
    h = len(tree_map)
    w = len(tree_map[0])
    max_scenic_score = 0

    for x, y in itertools.product(range(1, h - 1), range(1, w - 1)):
        scenic_score = get_scenic_score(tree_map, np.array([y, x]))
        max_scenic_score = max(max_scenic_score, scenic_score)

    print(max_scenic_score)
