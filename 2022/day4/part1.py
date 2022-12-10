if __name__ == "__main__":
    fully_contain = 0
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            left, right = line.split(",")
            left_range = [int(x) for x in left.split("-")]
            right_range = [int(x) for x in right.split("-")]

            if ((left_range[0] <= right_range[0]) and
                (left_range[1] >= right_range[1])):
                fully_contain += 1
            elif ((right_range[0] <= left_range[0]) and
                  (right_range[1] >= left_range[1])):
                fully_contain += 1

    print(fully_contain)
