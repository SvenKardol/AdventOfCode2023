from aocd import get_data
from collections import defaultdict

dataRaw = get_data(year=2023, day=8)

data = dataRaw.split("\n\n")

commands = data[0]
rooms = defaultdict()
for line in data[1].split("\n"):
    rooms[line.split()[0]] = [connecting_room.replace("(", "").replace(")", "").strip()
                              for connecting_room in line.split("=")[1].strip().split(",")]

print(rooms)

steps = 0
room = "AAA"
while room != "ZZZ":
    if commands[steps % len(commands)] == "L":
        room = rooms[room][0]
    else:
        room = rooms[room][1]
    steps += 1

print(steps)
