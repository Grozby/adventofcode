from typing import Tuple, Sequence

import numpy as np


def manhattan_distance(p1: np.ndarray, p2: np.ndarray) -> int:
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])


def in_bounds(pos: np.ndarray, h_max: int, w_max: int) -> bool:
    return 0 <= pos[0] < h_max and 0 <= pos[1] < w_max


class Node:

    def __init__(
        self,
        position: np.ndarray,
        distance_to_goal: int,
        cost: int,
    ):
        self.position = position
        self.distance_to_goal = distance_to_goal
        self.cost = cost

    @property
    def estimated_cost(self) -> int:
        return self.distance_to_goal + self.cost

    def __gt__(self, other):
        return self.estimated_cost > other.estimated_cost

    def __eq__(self, other):
        return self.estimated_cost == other.estimated_cost

    def get_neighbors(self) -> Sequence[np.ndarray]:
        return [
            self.position.copy() + (1, 0),
            self.position.copy() - (1, 0),
            self.position.copy() + (0, 1),
            self.position.copy() - (0, 1),
        ]


def parse_input() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    height_map = []
    starting_position = None
    goal_position = None

    with open("./input", "r") as f:
        line_count = 0
        while line := f.readline().rstrip():
            to_append = []
            for c_i, c in enumerate(line):
                if c == "S":
                    to_append.append(0)
                    starting_position = np.array((line_count, c_i))
                elif c == "E":
                    to_append.append(25)
                    goal_position = np.array((line_count, c_i))
                else:
                    to_append.append(ord(c) - 97)
            line_count += 1
            height_map.append(to_append)

    return np.array(height_map), starting_position, goal_position