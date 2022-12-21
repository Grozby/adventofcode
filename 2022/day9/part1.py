from dataclasses import dataclass

import numpy as np


@dataclass
class Move:
    direction: str
    n_steps: int


if __name__ == "__main__":
    direction_increments = {
        "L": np.array((0, -1)),
        "R": np.array((0, 1)),
        "U": np.array((1, 0)),
        "D": np.array((-1, 0)),
    }
    moves = []
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            direction, n_steps = line.split(" ")
            moves.append(Move(n_steps=int(n_steps), direction=direction))

    visited_by_tail = set()
    head = np.array((0, 0))
    tail = head.copy()

    for move in moves:
        for i in range(move.n_steps):
            head += direction_increments[move.direction]
            if any(np.abs(h - t) > 1 for h, t in zip(head, tail)):
                tail = head.copy() - direction_increments[move.direction]
            visited_by_tail.add(tuple(tail))

    print(len(visited_by_tail))
