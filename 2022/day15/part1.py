import numpy as np

from utils import parse_input

if __name__ == "__main__":
    sensors, beacons = parse_input("./input")

    x_max, y_max = 0, 0
    x_min, y_min = float("inf"), float("inf")

    for x, y in sensors + beacons:
        x_max, x_min = max(x_max, x), min(x_min, x)
        y_max, y_min = max(y_max, y), min(y_min, y)
    x_max += 4000000
    x_min -= 4000000
    y_row = 2000000
    b_set = set()
    y2k = np.zeros((x_max - x_min), dtype=np.uint8)
    beacons_on_y2k = 0
    for s, b in zip(sensors, beacons):
        if b[1] == y_row and tuple(b) not in b_set:
            b_set.add(tuple(b))
            beacons_on_y2k += 1
        distance = np.sum(np.abs(b - s))
        if (to_y2k := abs(y_row - s[1])) <= distance:
            distance -= to_y2k
            x_slice = slice(
                max(0, s[0] - distance - x_min),
                min(len(y2k), s[0] + distance + 1 - x_min),
            )
            y2k[x_slice] += 1

    print(len(y2k[y2k > 0]) - beacons_on_y2k)
