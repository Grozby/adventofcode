from utils import parse_input, check_pairs

if __name__ == "__main__":

    pair_packets = parse_input()

    sum_indices = 0
    for i, (pair1, pair2) in enumerate(pair_packets):
        if check_pairs(pair1, pair2) < 1:
            sum_indices += i + 1

    print(sum_indices)
