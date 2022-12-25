from utils import parse_input


def check_pairs(p1, p2) -> int:
    if isinstance(p1, int) and isinstance(p2, int):
        return p1 - p2

    if isinstance(p1, list) and isinstance(p2, int):
        p2 = [p2]
    if isinstance(p1, int) and isinstance(p2, list):
        p1 = [p1]

    for x1, x2 in zip(p1, p2):
        if (r := check_pairs(x1, x2)) != 0:
            return r

    return len(p1) - len(p2)


if __name__ == "__main__":

    pair_packets = parse_input()

    sum_indices = 0
    for i, (pair1, pair2) in enumerate(pair_packets):
        if check_pairs(pair1, pair2) < 1:
            sum_indices += i + 1

    print(sum_indices)
