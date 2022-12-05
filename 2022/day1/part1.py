from typing import List

if __name__ == "__main__":
    elfs: List[List[int]] = [[]]
    with open("./input", "r") as f:
        index = 0
        while line := f.readline():
            if line.rstrip() == "":
                index += 1
                elfs.append([])
            else:
                elfs[index].append(int(line))

    print(max([sum(e) for e in elfs]))
