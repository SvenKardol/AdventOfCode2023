import math

from aocd import get_data
from collections import defaultdict
dataRaw = get_data(year=2023, day=8)

data = dataRaw.split("\n\n")

commands = data[0]
rooms = defaultdict()
for line in data[1].split("\n"):
    rooms[line.split()[0]] = [connecting_room.replace("(", "").replace(")", "").strip()
                              for connecting_room in line.split("=")[1].strip().split(",")]

start_rooms = []
cycle_search = defaultdict()
index = 0
for room in rooms.keys():
    if room[2] == "A":
        start_rooms.append(room)
        cycle_search[index] = []
        index += 1

steps = 0
continue_search = True
while continue_search and steps < 1e5:
    continue_search = False
    for i in range(len(start_rooms)):
        room = start_rooms[i]
        start_rooms[i] = rooms[room][0] if commands[steps % len(commands)] == "L" else rooms[room][1]

        # If any of the rooms don't end in a "Z", then the search continues
        if start_rooms[i][2] != "Z":
            continue_search = True

        if start_rooms[i][2] == "Z":
            cycle_search[i].append(steps)

    steps += 1

cycles = []
for i in range(len(start_rooms)):
    # avoid first interval since it might not be the length of a full loop
    cycles.append((cycle_search[i][2] - cycle_search[i][1]))

print(math.lcm(*cycles))

# factorization of loop cycles
# 1, 53, 307, 16271
# 1, 79, 307, 24253
# 1, 43, 307, 13201
# 1, 47, 307, 14429
# 1, 59, 307, 18113
# 1, 73, 307, 22411

