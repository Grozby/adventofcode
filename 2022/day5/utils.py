from collections import defaultdict
from typing import Dict, List, Tuple


def parse_input():
    crates: Dict[str, List[str]] = defaultdict(lambda: [])
    moves: List[Tuple[int, str, str]] = []
    read_moves = False

    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            if not read_moves:
                if line[1] == "1":
                    f.readline()
                    read_moves = True
                else:
                    for i in range(1, len(line), 4):
                        if line[i] != " ":
                            crates[str(i // 4 + 1)].append(line[i])
            else:
                line = line[5:]
                _move, rest = line.split(" from ")
                _move = int(_move)
                _from, _to = rest.split(" to ")
                moves.append((_move, _from, _to))

    return crates, moves
