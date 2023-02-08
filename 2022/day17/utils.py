import functools
from dataclasses import dataclass
from typing import List

import numpy as np


class Rock:

    def __init__(self, comp: List[List[int]]):
        self.comp: np.array = np.array(comp)

    @functools.cached_property
    def width(self) -> int:
        return self.comp.shape[1]

    @functools.cached_property
    def height(self) -> int:
        return self.comp.shape[0]


@dataclass
class Position:
    x: int
    y: int


def check_overlap(chamber: np.array, rock: Rock, pos_y: int, pos_x: int):
    return np.any(chamber[pos_y:pos_y + rock.height, pos_x:pos_x + rock.width] +
                  rock.comp == 2)


ROCKS = [
    Rock(comp=[[1, 1, 1, 1]]),
    Rock(comp=[
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],),
    Rock(comp=[
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],),
    Rock(comp=[
        [1],
        [1],
        [1],
        [1],
    ],),
    Rock(comp=[
        [1, 1],
        [1, 1],
    ],),
]
