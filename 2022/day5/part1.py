from utils import parse_input

if __name__ == "__main__":
    crates, moves = parse_input()

    for (_n_move, _from, _to) in moves:
        for _ in range(_n_move):
            crates[_to].insert(0, crates[_from].pop(0))

    output = []
    for i in range(len(crates.keys())):

        if len(crates[(key := str(i + 1))]) != 0:
            output.append(crates[key][0])

    print("".join(output))
