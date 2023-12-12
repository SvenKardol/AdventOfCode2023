from collections import Counter
from functools import cache
from aocd import get_data

dataRaw = get_data(year=2023, day=12)
data = dataRaw.split("\n")


@cache
def find_possible_configurations(s, size_current_spring, springs_to_be_found):
    # End of string, check if there are no springs or that the current spring covers the last spring
    if len(s) == 0:
        # No springs to be found and current spring is empty.
        if size_current_spring == 0 and len(springs_to_be_found) == 0:
            return 1

        # 1 spring left to find, and the current spring is the size of the last spring.
        if len(springs_to_be_found) == 1 and size_current_spring == springs_to_be_found[0]:
            return 1

        # not compliant, return 0
        return 0

    # no springs left to find, but I have a current spring.
    if len(springs_to_be_found) == 0 and size_current_spring != 0:
        return 0

    possible_springs = sum([1 for ch in s if ch == '#' or ch == '?'])

    # possible springs to be found is less than total springs to be found
    if possible_springs + size_current_spring < sum(springs_to_be_found):
        return 0

    # current spring ends, but it's not the size of the spring to be found.
    if s[0] == '.' and size_current_spring != 0 and size_current_spring != springs_to_be_found[0]:
        return 0

    possibilities = 0

    # current spring ends by "." or "?"
    if s[0] == '.' or s[0] == '?':
        # spring has size 0 (no spring), find the same spring
        if size_current_spring == 0:
            possibilities += find_possible_configurations(s[1:], 0, springs_to_be_found)
        # spring is correct size. Search next spring
        elif size_current_spring == springs_to_be_found[0]:
            possibilities += find_possible_configurations(s[1:], 0, springs_to_be_found[1:])

    # current spring is extended by "#" or "?".
    if s[0] == '#' or s[0] == '?':
        possibilities += find_possible_configurations(s[1:], size_current_spring + 1, springs_to_be_found)

    return possibilities


def part2():
    total = 0
    for line in data:
        old_springs = line.split()[0]
        old_arrangements = line.split()[1]

        springs = old_springs
        arrangements = old_arrangements
        for i in range(4):
            springs += "?" + old_springs
            arrangements += "," + old_arrangements

        arrangements = tuple([int(l) for l in arrangements.split(",")])
        total += find_possible_configurations(springs, 0, arrangements)
    print(total)


def part1_not_brute_force():
    total = 0
    for line in data:
        springs = line.split()[0]
        arrangements = line.split()[1]
        arrangements = tuple([int(l) for l in arrangements.split(",")])
        total += find_possible_configurations(springs, 0, arrangements)
    print(total)


part1_not_brute_force()
part2()
