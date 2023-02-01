import itertools
from copy import copy
from typing import Set, List, Dict, Tuple

from utils import parse_input, distance


class Agent:

    def __init__(
        self,
        name: str,
        valve_name: str,
        can_move_in: int = 0,
        pressure_to_add: int = 0,
    ):
        self.name = name
        self.valve_name = valve_name
        self.can_move_in = can_move_in
        self.pressure_to_add = pressure_to_add


class Node:

    def __init__(
        self,
        parent,
        time: int,
        released_pressure: int,
        opened_valves: Set[str],
        agents: Dict[str, Agent],
    ):
        self.parent = parent
        self.time = time
        self.released_pressure = released_pressure
        self.opened_valves = opened_valves
        self.agents = agents

    def final_pressure(self) -> int:
        pressure = self.released_pressure
        for agent in self.agents.values():
            if agent.valve_name in self.opened_valves and agent.can_move_in > 0:
                pressure += agent.pressure_to_add
        return pressure


def part_2(input_path: str = "./input"):
    valves = parse_input(input_path)
    distances = distance(valves)

    max_valve_flow_rate = max([v.flow_rate for v in valves.values()])

    max_pressure = 0
    frontier = [
        Node(
            parent=None,
            time=26,
            released_pressure=0,
            opened_valves=set(
                v.name for v in valves.values() if v.flow_rate == 0),
            agents={
                "Grozby":
                    Agent(
                        name="Grozby",
                        valve_name=list(valves.keys())[0],
                    ),
                "Elephant":
                    Agent(
                        name="Elephant",
                        valve_name=list(valves.keys())[0],
                    ),
            },
        )
    ]

    while len(frontier) != 0:
        state = frontier.pop()

        if max_pressure != 0 and state.released_pressure + (max_valve_flow_rate * state.time) * 4 < max_pressure:
            continue

        active_agents = {
            a.name: a for a in state.agents.values() if a.can_move_in == 0
        }

        assert len(active_agents) > 0
        agent_flows = []
        for agent in active_agents.values():
            agent_flows.append([(
                v,
                distances[agent.valve_name][v.name] + 1,
            ) for v_n, v in valves.items() if v_n not in state.opened_valves])

        added = False
        for flows in itertools.product(*agent_flows):
            # If flows have some overlap in valves
            if len(agent_flows) != len(set(v.name for v, _ in flows)):
                # If the number of remaining valves to open is greater than the number of agents available
                if (remaining_valves := len(valves) -
                        len(state.opened_valves)) >= len(agent_flows):
                    max_pressure = max(max_pressure, state.final_pressure())
                    continue
                else:
                    flows = sorted(flows, key=lambda x: x[1])[:remaining_valves]
            if all(state.time - s - 1 < 0 for _, s in flows):
                max_pressure = max(max_pressure, state.final_pressure())
                continue

            added = True

            non_active_agents = {
                a.name: Agent(
                    name=a.name,
                    valve_name=a.valve_name,
                    can_move_in=a.can_move_in,
                    pressure_to_add=a.pressure_to_add,
                ) for a in state.agents.values() if a.name not in active_agents
            }
            new_active_agents = {
                a.name: Agent(
                    name=a.name,
                    valve_name=v.name,
                    can_move_in=s,
                    pressure_to_add=max(v.flow_rate * (state.time - s), 0),
                ) for a, (v, s) in zip(active_agents.values(), flows)
            }
            new_agents = new_active_agents | non_active_agents

            min_steps = min(a.can_move_in for a in new_agents.values())
            for a in new_agents.values():
                a.can_move_in -= min_steps

            pressure_to_add = sum(a.pressure_to_add
                                  for a in new_agents.values()
                                  if a.can_move_in == 0)
            opened_valves = state.opened_valves.copy()
            for a in new_agents.values():
                opened_valves.add(a.valve_name)

            frontier.append(
                Node(
                    parent=state,
                    time=state.time - min_steps,
                    released_pressure=state.released_pressure + pressure_to_add,
                    opened_valves=opened_valves,
                    agents=new_agents,
                ))

        if not added:
            max_pressure = max(max_pressure, state.final_pressure())

    return max_pressure


if __name__ == "__main__":
    print(part_2("./input_test"))
    print(part_2())
