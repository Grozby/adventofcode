import string

if __name__ == "__main__":
    priorities = 0
    characters = string.ascii_lowercase + string.ascii_uppercase
    with open("./input", "r") as f:
        index = 0
        while (l1 := f.readline().rstrip()) and (l2 := f.readline().rstrip()) and (l3 := f.readline().rstrip()):
            c = set(l1).intersection(set(l2)).intersection(set(l3)).pop()
            priorities += characters.index(c) + 1

    print(priorities)
