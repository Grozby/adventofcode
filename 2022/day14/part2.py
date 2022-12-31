import numpy as np

from utils import parse_input, populate_map

if __name__ == "__main__":

    rock_structures, (x_max, x_min, y_max) = parse_input()

    y_max += 3
    x_max += 500
    scan_map = populate_map(
        scan_map=np.zeros((
            y_max,
            x_max,
        )),
        rock_structures=rock_structures,
    )

    scan_map[-1, :] = 1

    total_sand = 0
    can_drop = True
    while can_drop:
        can_drop = False
        s = np.array((0, 500))

        while scan_map[s[0], s[1]] == 0:
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
