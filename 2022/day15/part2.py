import itertools

import numpy as np

from utils import parse_input


def manhattan_distance(p1: np.ndarray, p2: np.ndarray):
    return np.sum(np.abs(p1 - p2))


if __name__ == "__main__":
    sensors, beacons = parse_input("./input")

    r = 4000000
    distances = []
    p45, m45 = [], []
    for s, b in zip(sensors, beacons):
        s_x, s_y = s

        distance = manhattan_distance(s, b)
        distances.append(distance)
        p45.append(s_y - s_x + distance + 1)
        p45.append(s_y - s_x - distance - 1)
        m45.append(s_y + s_x + distance + 1)
        m45.append(s_y + s_x - distance - 1)

    for q_l1, q_l2 in itertools.product(p45, m45):

        intersect_point = np.array(((q_l2 - q_l1) // 2, (q_l2 + q_l1) // 2))
        if (all(0 <= i < r for i in intersect_point) and all(
                manhattan_distance(intersect_point, s) > d
                for s, d in zip(sensors, distances))):
            print(4000000 * intersect_point[0] + intersect_point[1])
            break
