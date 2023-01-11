import itertools
from collections import defaultdict
from typing import List, Dict


class Valve:

    def __init__(self, name: str, flow_rate: float, valves: List[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.valves = valves


def distance(valves: Dict[str, Valve]) -> Dict[str, Dict[str, int]]:
    """Floyd-Warshall"""
    dist = defaultdict(lambda: {})

    for v1 in valves.values():
        dist[v1.name][v1.name] = 0
        for v2 in v1.valves:
            dist[v1.name][v2] = 1
        for v2 in set(valves.keys()) - set(v1.valves):
            dist[v1.name][v2] = float("inf")

    for (k, i, j) in itertools.product(valves.keys(), repeat=3):
        if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def parse_input(input_filename: str = "./input") -> Dict[str, Valve]:
    valves = {}

    with open(input_filename, "r") as f:
        while line := f.readline().rstrip():
            line = line.replace("Valve ", "")
            name, line = line.split(" has flow rate=")
            if "valves" in line:
                flow_rate, line = line.split("; tunnels lead to valves ")
                to_valves = line.split(", ")
            else:
                flow_rate, to_valves = line.split("; tunnel leads to valve ")
                to_valves = [to_valves]

            valves[name] = Valve(
                name=name,
                flow_rate=float(flow_rate),
                valves=to_valves,
            )

    return valves
