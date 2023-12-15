from aocd import get_data
import numpy as np


def slide_rocks(d):
    # dish is always tilting east (because we rotate first)
    # just keep replacing O. with .0 as all the rocks slide to the right
    d2 = ["".join(l) for l in d]
    for y in range(len(d2)):
        while "O." in d2[y]:
            d2[y] = d2[y].replace("O.", ".O")
    return [[char for char in s] for s in d2]


def rotate(d):
    p = np.array(d)
    d = list(np.rot90(p, 1, (1, 0)))
    return d


def score(d):
    total_leverage = 0
    for y, row in enumerate(d):
        for x, ch in enumerate(row):
            if ch == "O":
                total_leverage += len(row) - y
    return total_leverage


def print_data(d):
    for line in d:
        print("".join(line))
    print("")


def cycle_data(d):
    for _ in range(4):
        d = rotate(d)
        d = slide_rocks(d)
    return d


def find_pattern(d):
    current_cycle = 0
    states = [d]

    while True:
        current_data = cycle_data(states[current_cycle])

        if current_data in states:
            sc = states.index(current_data)
            p = current_cycle + 1 - states.index(current_data)
            return sc, p, states

        states.append(current_data)
        current_cycle += 1


def part2():
    data_raw = get_data(year=2023, day=14)
    data = [[char for char in s] for s in data_raw.split("\n")]
    start_cycle, period, s = find_pattern(data)
    target = int(1e9)
    print(score(s[(target - start_cycle) % period + start_cycle]))


part2()
