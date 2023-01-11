from typing import Set, List

from utils import parse_input, distance


class Node:

    def __init__(
        self,
        parent,
        valve_name: str,
        time: int,
        released_pressure: int,
        opened_valves: Set[str],
        order_opened_valves: List[str],
    ):
        self.parent = parent
        self.valve_name = valve_name
        self.time = time
        self.released_pressure = released_pressure
        self.opened_valves = opened_valves.copy()
        self.opened_valves.add(valve_name)
        self.order_opened_valves = order_opened_valves


def part_1(input_path: str = "./input"):
    valves = parse_input(input_path)
    distances = distance(valves)

    final_states = []
    frontier = [
        Node(
            parent=None,
            valve_name=list(valves.keys())[0],
            time=30,
            released_pressure=0,
            opened_valves=set(
                v.name for v in valves.values() if v.flow_rate == 0),
            order_opened_valves=[],
        )
    ]

    while len(frontier) != 0:
        state = frontier.pop()

        flows = [(
            v,
            (d := distances[state.valve_name][v.name]),
            int(v.flow_rate * (state.time - d - 1)),
        ) for v_n, v in valves.items() if v_n not in state.opened_valves]

        added = False
        for valve, steps, pressure in flows:
            if state.time - steps - 1 < 0:
                continue
            added = True
            frontier.append(
                Node(
                    parent=state,
                    valve_name=valve.name,
                    time=state.time - steps - 1,
                    released_pressure=state.released_pressure + pressure,
                    opened_valves=state.opened_valves,
                    order_opened_valves=state.order_opened_valves +
                    [valve.name],
                ))
        if not added:
            final_states.append(state)

    return max(
        final_states,
        key=lambda x: x.released_pressure,
    ).released_pressure


if __name__ == "__main__":
    print(part_1("./input_test"))
    print(part_1())
