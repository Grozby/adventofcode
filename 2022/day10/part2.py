import abc


class Instruction(abc.ABC):

    @property
    @abc.abstractmethod
    def cycles(self) -> int:
        pass

    @abc.abstractmethod
    def execute(self, register: int) -> int:
        pass

    @classmethod
    def from_string(cls, line: str):
        if line == "noop":
            return NoOp()
        elif line.startswith("addx"):
            return AddX(value=int(line.split(" ")[1]))
        else:
            raise RuntimeError(f"Only instruction `noop` and `addx` "
                               f"are supported, not {line}")


class NoOp(Instruction):

    @property
    def cycles(self) -> int:
        return 1

    def execute(self, register: int) -> int:
        return register


class AddX(Instruction):

    def __init__(self, value: int):
        self.value = value

    @property
    def cycles(self) -> int:
        return 2

    def execute(self, register: int) -> int:
        return register + self.value


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
