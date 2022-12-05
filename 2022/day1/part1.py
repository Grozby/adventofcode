from typing import List

if __name__ == "__main__":
    elfs: List[List[int]] = [[]]
    max_elf = 0
    with open("./input", "r") as f:
        index = 0
        while line := f.readline():
            if line.rstrip() == "":
                max_elf = max(max_elf, sum(elfs[index]))
                index += 1
                elfs.append([])
            else:
                elfs[index].append(int(line))

    print(max_elf)
