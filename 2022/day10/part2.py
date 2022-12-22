from utils import Instruction

if __name__ == "__main__":

    instructions = []
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            instructions.append(Instruction.from_string(line))

    display = [["" for _ in range(40)] for _ in range(6)]
    r = 1
    cycle = 0

    for instruction in instructions:
        for _ in range(instruction.cycles):
            row = cycle // 40
            col = cycle % 40
            display[row][col] = "#" if r - 1 <= (cycle % 40) <= r + 1 else "."
            cycle += 1
        r = instruction.execute(r)

    for r in display:
        print("".join(r))
