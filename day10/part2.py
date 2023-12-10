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


def find_loop(start_pos):
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
            return position_dict
        else:
            position_dict[lhs] = position_dict[prev_lhs] + 1

        next_rhs = next_pos(prev_rhs, rhs)
        prev_rhs = rhs
        rhs = next_rhs

        if rhs in position_dict:
            return position_dict
        else:
            position_dict[rhs] = position_dict[prev_rhs] + 1


def remove_junk(data, position_dict):
    clear_data = []
    for y in range(len(data)):
        new_line = ""
        for x in range(len(data[y])):
            if (x, y) in position_dict:
                new_line += data[y][x]
            else:
                new_line += "."
        clear_data.append(new_line)

    return clear_data


start_pos = search_start()
position_dict = find_loop(search_start())

# clear junk from input
cleared_data = remove_junk(data, position_dict)

# In order to be in a closed loop, you need an odd number of loop crossings to occur before your spot
# Loop crossings only happen when the character is "closed on top side (since we go from top to bottom)
# This means either F, |, or 7.
# L and J are bottom closed", which means you don't leave the loop.
#  ..F-7..
#  .FJ.L7.
#  .L---J.
# Dot in the middle is in the loop, because F is in front. J doesn't cause a loop crossing as seen here.
in_loop = 0
for y in range(len(cleared_data)):
    loop_crossings = 0
    for x in range(len(cleared_data[y])):
        if cleared_data[y][x] == ".":
            if loop_crossings % 2 == 1:
                in_loop += 1
        else:
            if cleared_data[y][x] in ["F", "|", "7"]:
                loop_crossings += 1

print(in_loop)
