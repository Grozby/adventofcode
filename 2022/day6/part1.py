if __name__ == "__main__":
    with open("./input", "r") as f:
        line = f.readline().rstrip()

    characters = line[:4]
    i = 4
    while i < len(line) and len(set(characters)) != 4:
        i += 1
        characters = line[i - 4:i]
    print(i)
