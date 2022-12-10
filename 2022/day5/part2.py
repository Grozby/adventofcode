from utils import parse_input

if __name__ == "__main__":
    crates, moves = parse_input()

    for (_n_move, _from, _to) in moves:
        to_move = crates[_from][:_n_move]
        crates[_from] = crates[_from][_n_move:]
        to_move.extend(crates[_to])
        crates[_to] = to_move

    output = []
    for i in range(len(crates.keys())):
        if len(crates[(key := str(i + 1))]) != 0:
            output.append(crates[key][0])

    print("".join(output))
