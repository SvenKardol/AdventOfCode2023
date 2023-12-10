from aocd import get_data
from collections import defaultdict

dataRaw = get_data(year=2023, day=10)
data = dataRaw.split("\n")


def search_start():
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                return (x, y)


def next_pos_both(curr, pipe_type):
    match pipe_type:
        case "|":
            pos1 = (curr[0], curr[1] + 1)
            pos2 = (curr[0], curr[1] - 1)

        case "-":
            pos1 = (curr[0] + 1, curr[1])
            pos2 = (curr[0] - 1, curr[1])

        case "L":
            pos1 = (curr[0] + 1, curr[1])
            pos2 = (curr[0], curr[1] - 1)

        case "J":
            pos1 = (curr[0] - 1, curr[1])
            pos2 = (curr[0], curr[1] - 1)

        case "7":
            pos1 = (curr[0] - 1, curr[1])
            pos2 = (curr[0], curr[1] + 1)

        case "F":
            pos1 = (curr[0] + 1, curr[1])
            pos2 = (curr[0], curr[1] + 1)

    return pos1, pos2


def next_pos(prev, curr):
    pos1, pos2 = next_pos_both(curr, data[curr[1]][curr[0]])
    return pos1 if pos1 != prev else pos2


def determine_start_pipe_type(start_pos):
    for pipe_type in "|-LJ7F"[::1]:
        pos1, pos2 = next_pos_both(start_pos, pipe_type)
        if start_pos in next_pos_both(pos1, data[pos1[1]][pos1[0]]) and \
                start_pos in next_pos_both(pos2, data[pos2[1]][pos2[0]]):
            data[start_pos[1]] = data[start_pos[1]].replace("S", pipe_type)
            return pos1, pos2


def find_furthest_from_start(start_pos):
    position_dict = defaultdict()
    position_dict[start_pos] = 0
    prev_lhs = start_pos
    prev_rhs = start_pos

    # S was an F shape for my input: Determine left hand side and right hand side of the loop.
    lhs, rhs = determine_start_pipe_type(start_pos)
    position_dict[lhs] = 1
    position_dict[rhs] = 1
    while True:
        next_lhs = next_pos(prev_lhs, lhs)
        prev_lhs = lhs
        lhs = next_lhs

        if lhs in position_dict:
            return position_dict[lhs]
        else:
            position_dict[lhs] = position_dict[prev_lhs] + 1

        next_rhs = next_pos(prev_rhs, rhs)
        prev_rhs = rhs
        rhs = next_rhs

        if rhs in position_dict:
            return position_dict[rhs]
        else:
            position_dict[rhs] = position_dict[prev_rhs] + 1


start_pos = search_start()
furthest_from_start = find_furthest_from_start(search_start())

print(furthest_from_start)
