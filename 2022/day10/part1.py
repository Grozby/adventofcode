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

    target_cycle = 20
    signal_strength = 0
    register = 1
    cycle_count = 0
    for i_count, instruction in enumerate(instructions):
        cycle_count += instruction.cycles
        if cycle_count >= target_cycle:
            signal_strength += register * target_cycle
            register = instruction.execute(register)
            target_cycle += 40
        else:
            register = instruction.execute(register)

    print(signal_strength)
