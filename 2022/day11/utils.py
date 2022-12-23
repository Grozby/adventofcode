from functools import partial
from typing import Callable, List, Tuple


class Monkey:

    def __init__(
        self,
        starting_items: List[int],
        divisible_by: int,
        operation: Callable,
        monkey_if_true: int,
        monkey_if_false: int,
    ):
        self.items = starting_items
        self.divisible_by = divisible_by
        self.operation = operation
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.items_inspected = 0

    def add_item(self, item: int):
        self.items.append(item)

    def items_to_throw(self) -> List[Tuple[int, int]]:
        monkey_items = []
        for item in self.items:
            item = self.operation(item) // 3
            if item % self.divisible_by == 0:
                monkey_items.append((self.monkey_if_true, item))
            else:
                monkey_items.append((self.monkey_if_false, item))
        self.items_inspected += len(self.items)
        self.items.clear()
        return monkey_items


def parse_input() -> List[Monkey]:
    monkeys = []
    with open("./input", "r") as f:
        f.readline()
        while line := f.readline().rstrip():
            line = line.replace("Starting items: ", "")
            items = [int(x) for x in line.split(", ")]
            line = f.readline().rstrip().lstrip().replace(
                "Operation: new = old ", "")
            if line[2:] == "old" and line[0] == "*":
                operation = lambda x: x * x
            elif line[2:] == "old" and line[0] == "*":
                operation = lambda x: x + x
            elif line[0] == "*":
                operation = partial(lambda x, i: x * i, i=int(line[2:]))
            elif line[0] == "+":
                operation = partial(lambda x, i: x + i, i=int(line[2:]))
            else:
                raise RuntimeError()

            div = int(f.readline().rstrip().replace("Test: divisible by ", ""))
            if_true_monkey = int(f.readline().rstrip().replace(
                "If true: throw to monkey ", ""))
            if_false_monkey = int(f.readline().rstrip().replace(
                "If false: throw to monkey ", ""))
            monkeys.append(
                Monkey(
                    starting_items=items,
                    divisible_by=div,
                    operation=operation,
                    monkey_if_true=if_true_monkey,
                    monkey_if_false=if_false_monkey,
                ))
            f.readline()
            f.readline()
    return monkeys
