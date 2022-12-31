from typing import List, Sequence

import numpy as np


def _parse_coordinates(x: str) -> np.ndarray:
    bx, by = x.split(", ")
    return np.array((
        int(bx.replace("x=", "")),
        int(by.replace("y=", "")),
    ))


def parse_input(input_filename: str = "./input") -> Sequence[List[np.ndarray]]:
    sensors = []
    beacons = []

    with open(input_filename, "r") as f:
        while line := f.readline().rstrip():
            line = line.replace("Sensor at ", "")
            sensor, beacon = [
                _parse_coordinates(x)
                for x in line.split(": closest beacon is at ")
            ]
            sensors.append(sensor)
            beacons.append(beacon)

    return sensors, beacons
