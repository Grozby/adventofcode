import string

if __name__ == "__main__":
    offset = string.ascii_uppercase.index("X")
    score = 0
    with open("./input", "r") as f:
        index = 0
        while line := f.readline().rstrip():
            other_move = string.ascii_uppercase.index(line[0])
            decision = string.ascii_uppercase.index(line[2]) - offset
            our_move = (other_move + (decision - 1)) % 3

            score += our_move + 1
            if our_move == (other_move + 1) % 3:
                score += 6
            elif our_move == other_move:
                score += 3

    print(score)
