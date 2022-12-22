from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set, Tuple, Optional

import numpy as np


@dataclass
class Move:
    direction: str
    n_steps: int


class RopeNode:

    def __init__(self,
                 position: np.ndarray,
                 next_node: Optional[RopeNode] = None):
        self.position = position
        self.next_node = next_node


class Rope:

    def __init__(self, length: int = 2):
        assert length > 1

        self.visited_by_tail: Set[Tuple] = set()
        self.head = RopeNode(position=np.array((0, 0)))

        h = self.head
        for _ in range(length - 1):
            h.next_node = RopeNode(position=np.array((0, 0)))
            h = h.next_node
        self.tail = h

    def update_head(self, direction: np.ndarray):
        self.head.position += direction

        p = self.head
        n = self.head.next_node
        while n is not None:
            new_p = p.position.copy()
            needs_update = False
            for i in range(2):
                if np.abs(p.position[i] - n.position[i]) > 1:
                    needs_update = True
                    new_p[i] -= 1 if p.position[i] > n.position[i] else -1
            if needs_update:
                n.position = new_p

            p = n
            n = n.next_node
        self.visited_by_tail.add(tuple(p.position))

    def print_map(self, size: Tuple[int, int], step: int):
        m = [["." for _ in range(size[0])] for _ in range(size[1])]

        h = self.head
        m[h.position[0]][h.position[1]] = "H"

        h = h.next_node
        count = 1
        while h.next_node is not None:
            if m[h.position[0]][h.position[1]] == ".":
                m[h.position[0]][h.position[1]] = str(count)
            h = h.next_node
            count += 1

        print(f"--- Step: {step}")
        for row in m[::-1]:
            print(row)


def parse_input() -> List[Move]:
    moves = []
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            direction, n_steps = line.split(" ")
            moves.append(Move(n_steps=int(n_steps), direction=direction))
    return moves


if __name__ == "__main__":
    direction_increments = {
        "L": np.array((0, -1)),
        "R": np.array((0, 1)),
        "U": np.array((1, 0)),
        "D": np.array((-1, 0)),
    }

    moves = parse_input()
    rope = Rope(length=10)

    step_count = 0
    for m_count, move in enumerate(moves):
        for i in range(move.n_steps):
            rope.update_head(direction_increments[move.direction])
            # rope.print_map(size=(6, 5), step=(step_count := step_count + 1))

    print(len(rope.visited_by_tail))
