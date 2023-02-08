import itertools
from typing import List

import numpy as np

from utils import ROCKS, Position, Rock, check_overlap


def part_1(input_path: str = "./input"):
    list_moves: List[str] = []
    with open(input_path, "r") as f:
        while line := f.readline().rstrip():
            list_moves.extend(list(line))

    chamber = np.zeros((5000, 7), np.int8)
    chamber[0, :] = 1

    max_height = 0
    rocks = itertools.cycle(ROCKS)
    moves = itertools.cycle(list_moves)

    rock: Rock = next(rocks)
    pos = Position(x=2, y=max_height + 4)
    rock_count = 0

    while rock_count < 2022:
        move = next(moves)
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
            chamber[pos.y:pos.y + rock.height, pos.x:pos.x + rock.width] += rock.comp
            max_height = max(
                *[j + pos.y for j in range(rock.height) if np.any(chamber[pos.y + j, :] == 1)],
                max_height
            )
            rock = next(rocks)
            pos = Position(x=2, y=max_height + 4)
            rock_count += 1
        else:

            pos.y -= 1
            assert pos.y > -1

    return max_height


if __name__ == "__main__":
    print(part_1("./input_test"))
    print(part_1())
