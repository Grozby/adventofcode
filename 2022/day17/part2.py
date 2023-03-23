import itertools
from dataclasses import dataclass
from typing import List, Tuple, NamedTuple

import numpy as np

from utils import ROCKS, Position, Rock, check_overlap


@dataclass
class State:
    rock_count: int
    height: int


def part_2(input_path: str = "./input"):
    list_moves: List[str] = []
    with open(input_path, "r") as f:
        while line := f.readline().rstrip():
            list_moves.extend(list(line))

    states = {}
    chamber = np.zeros((20000, 7), np.int8)
    chamber[0, :] = 1

    max_height = 0
    rocks = itertools.cycle(enumerate(ROCKS))
    moves = itertools.cycle(enumerate(list_moves))

    n_rocks = 1000000000000
    (ri, rock) = next(rocks)
    pos = Position(x=2, y=max_height + 4)
    rock_count = 0

    while True:
        mi, move = next(moves)
        match move:
            case ">":
                if ((x := pos.x + 1) + rock.width <= chamber.shape[1] and
                        not check_overlap(
                            chamber=chamber,
                            rock=rock,
                            pos_x=x,
                            pos_y=pos.y,
                        )):
                    pos.x += 1

            case "<":
                if ((x := pos.x - 1) >= 0 and
                        not check_overlap(
                            chamber=chamber,
                            rock=rock,
                            pos_x=x,
                            pos_y=pos.y,
                        )):
                    pos.x -= 1
            case _:
                raise RuntimeError("Accepted letters as input are `<` and `>`.")

        if check_overlap(
                chamber=chamber,
                rock=rock,
                pos_x=pos.x,
                pos_y=pos.y - 1,
        ):
            chamber[pos.y:pos.y + rock.height,
                    pos.x:pos.x + rock.width] += rock.comp
            max_height = max(
                max_height,
                *[
                    j + pos.y
                    for j in range(rock.height)
                    if np.any(chamber[pos.y + j, :] == 1)
                ],
            )
            rock_count += 1
            if (s := states.get((ri, mi))) is not None:
                cycle = rock_count - s.rock_count
                missing_rocks = n_rocks - rock_count
                if missing_rocks % cycle == 0:
                    return ((max_height - s.height) * ((missing_rocks // cycle) + 1) +
                            s.height)
            states[(ri, mi)] = State(
                rock_count=rock_count,
                height=max_height,
            )
            ri, rock = next(rocks)
            pos = Position(x=2, y=max_height + 4)

        else:
            pos.y -= 1
            assert pos.y > -1

    return max_height


if __name__ == "__main__":
    print(part_2("./input_test"))
    print(part_2())
