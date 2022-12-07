import string

if __name__ == "__main__":
    priorities = 0
    characters = string.ascii_lowercase + string.ascii_uppercase
    with open("./input", "r") as f:
        index = 0
        while line := f.readline().rstrip():
            length = len(line) // 2
            c = set(line[:length]).intersection(set(line[length:])).pop()
            priorities += characters.index(c) + 1

    print(priorities)
