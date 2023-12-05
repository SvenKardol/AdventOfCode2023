from aocd import get_data
from functools import cache

dataRaw = get_data(year=2023, day=5)


def intersect(start_range, end_range, convert_start_range, convert_end_range):
    return not (end_range < convert_start_range or convert_end_range < start_range)


def intersect_ranges(range_seed, line):
    return intersect(range_seed[0], range_seed[1], line[1], line[1] + line[2])


def convert_range(original_range, table):
    new_ranges = []
    converted_ranges = []
    for line in table:
        if intersect_ranges(original_range, line):
            start_range = original_range[0] if original_range[0] > line[1] else line[1]
            end_range = original_range[1] if original_range[1] < line[1] + line[2] else line[1] + line[2] - 1
            new_range = [start_range, end_range]
            new_ranges.append(new_range)
            converted_range = [line[0] + start_range - line[1], line[0] + end_range - line[1]]
            converted_ranges.append(converted_range)

    minim = original_range[0]
    sorted_ranges = sorted(new_ranges, key=lambda x: x[0])

    # add range that was not covert by the conversions
    for original_range in sorted_ranges:
        if minim == original_range[0]:
            minim = original_range[1] + 1
        else:
            converted_ranges.append([minim, original_range[0] - 1])
            minim = original_range[0]

    # add the tail range if it's not covered by the conversions
    if minim < original_range[1]:
        converted_ranges.append([minim, original_range[1]])

    return converted_ranges


def get_seeds():
    return [int(seed) for seed in dataRaw.split("\n")[0].split("seeds: ")[1].split()]


@cache
def get_conversions():
    split_data = dataRaw.split("\n\n")
    conversions = []
    for i in range(1, len(split_data)):
        conversions.append([[int(x) for x in s.split()] for s in split_data[i].split("\n")[1:]])
    return conversions


def convert_values(original_values, conversions):
    return_values = original_values
    for c in conversions:
        new_values = []
        for s in return_values:
            new_ranges = convert_range(s, c)
            new_values.extend(new_ranges)

        return_values = new_values

    return sorted(return_values, key=lambda x: x[0])


seeds = get_seeds()
least = -1
index = 1
while index < len(seeds):
    original_seeds = [[seeds[index - 1], seeds[index - 1] + seeds[index]]]
    index += 2
    ranges = convert_values(original_seeds, get_conversions())

    if least == -1 or ranges[0][0] < least:
        least = ranges[0][0]

print(least)
