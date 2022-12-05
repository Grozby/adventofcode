from typing import List

if __name__ == "__main__":
    elfs: List[List[int]] = [[]]
    max_elfs = [0, 0, 0]
    with open("./input", "r") as f:
        index = 0
        while line := f.readline():
            if line.rstrip() == "":
                if (elf := sum(elfs[index])) > max_elfs[-1]:
                    max_elfs[-1] = elf
                    max_elfs.sort(reverse=True)
                index += 1
                elfs.append([])
            else:
                elfs[index].append(int(line))

    print(sum(max_elfs))
