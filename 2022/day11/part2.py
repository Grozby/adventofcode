from typing import List

from utils import Monkey, parse_input


def print_monkey_items(monkeys: List[Monkey], r: int):
    print(f"Round {r} \t =============")
    for i, m in enumerate(monkeys):
        print(f"Monkey {i}: {', '.join([str(x) for x in m.items])}")


if __name__ == "__main__":

    monkeys: List[Monkey] = parse_input()
    monkey_inspected_items = [0 for _ in range(len(monkeys))]
    for r in range(10000):
        for monkey in monkeys:
            items_to_throw = monkey.items_to_throw(divided_by=1)
            for monkey_index, item in items_to_throw:
                monkeys[monkey_index].add_item(item)
        # print_monkey_items(monkeys, r)

    monkeys = sorted(monkeys, key=lambda x: x.items_inspected, reverse=True)
    print(monkeys[0].items_inspected * monkeys[1].items_inspected)
