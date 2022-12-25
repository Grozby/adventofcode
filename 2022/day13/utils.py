from typing import List


def parse_line(x: str):
    if x == "":
        return []

    packets = []
    only_numeric = True
    count, s_i = 0, 0
    for i, c in enumerate(x):
        if c == "[":
            count += 1
            if count == 1:
                s_i = i
            only_numeric = False
        elif c == "]":
            count -= 1
            if count == 0:
                packets.append(parse_line(x[s_i + 1:i]))
                s_i = i + 1
        elif c == "," and count == 0:
            if only_numeric:
                packets.append(int(x[s_i:i]))
            s_i = i + 1
            only_numeric = True

    if x[s_i:] != "":
        packets.append(int(x[s_i:]))
    return packets


def parse_input() -> List:
    pair_packets = []

    with open("./input", "r") as f:
        while line1 := f.readline().rstrip():
            line2 = f.readline().rstrip()
            pair_packets.append((
                parse_line(line1[1:-1]),
                parse_line(line2[1:-1]),
            ))
            f.readline()

    return pair_packets
