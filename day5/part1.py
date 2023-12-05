from aocd import get_data
from functools import cache
dataRaw = get_data(year=2023, day=5)


def convert_num(num, table):
    for line in table:
        if line[1] <= num <= line[1] + line[2]:
            return line[0] + num - line[1]

    return num


def get_seeds():
    return [int(seed) for seed in dataRaw.split("\n")[0].split("seeds: ")[1].split()]


@cache
def get_conversions():
    split_data = dataRaw.split("\n\n")
    conversions = []
    for i in range(1, len(split_data)):
        conversions.append([[int(x) for x in s.split()] for s in split_data[i].split("\n")[1:]])
    return conversions


least = -1
for seed in get_seeds():
    outcome = seed
    for c in get_conversions():
        outcome = convert_num(outcome, c)

    if least == -1 or outcome < least:
        least = outcome

print(least)
