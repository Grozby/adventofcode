from utils import Instruction

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
