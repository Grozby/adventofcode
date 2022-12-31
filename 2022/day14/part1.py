import numpy as np

from utils import parse_input, populate_map

if __name__ == "__main__":

    rock_structures, (x_max, x_min, y_max) = parse_input()

    scan_map = populate_map(
        scan_map=np.zeros((
            y_max + 1,
            x_max + 1,
        )),
        rock_structures=rock_structures,
    )

    total_sand = 0
    can_drop = True
    while can_drop:
        can_drop = False
        s = np.array((0, 500))

        while s[0] <= y_max and x_min < s[1] < x_max:
            if scan_map[s[0] + 1, s[1]] == 0:
                s += (1, 0)
            elif scan_map[s[0] + 1, s[1] - 1] == 0:
                s += (1, -1)
            elif scan_map[s[0] + 1, s[1] + 1] == 0:
                s += (1, 1)
            else:
                can_drop = True
                total_sand += 1
                scan_map[s[0], s[1]] = 2
                break

    print(total_sand)
