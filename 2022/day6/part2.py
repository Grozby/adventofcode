if __name__ == "__main__":
    with open("./input", "r") as f:
        line = f.readline().rstrip()

    characters = line[:14]
    i = 14
    while i < len(line) and len(set(characters)) != 14:
        i += 1
        characters = line[i - 14:i]
    print(i)
