if __name__ == "__main__":
    n_overlap = 0

    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            left, right = line.split(",")
            left_range = [int(x) for x in left.split("-")]
            right_range = [int(x) for x in right.split("-")]

            max_low = max(left_range[0], right_range[0])
            min_high = min(left_range[1], right_range[1])

            if max_low <= min_high:
                n_overlap += 1

    print(n_overlap)
