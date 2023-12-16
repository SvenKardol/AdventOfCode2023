from aocd import get_data
dataRaw = get_data(year=2023, day=16)
data = dataRaw.split("\n")


def next_beam(x, y, d):
    command = data[y][x]

    if command == ".":
        if d in "LR":
            new_x = x + 1 if d == "R" else x - 1
            return [[(new_x, y), d]]
        if d in "UD":
            new_y = y + 1 if d == "D" else y - 1
            return [[(x, new_y), d]]
    elif command == "|":
        if d in "UD":
            new_y = y + 1 if d == "D" else y - 1
            return [[(x, new_y), d]]
        else:
            new_beam1 = [(x, y - 1), "U"]
            new_beam2 = [(x, y + 1), "D"]
            return [new_beam1, new_beam2]
    elif command == "-":
        if d in "LR":
            new_x = x + 1 if d == "R" else x - 1
            return [[(new_x, y), d]]
        else:
            new_beam1 = [(x - 1, y), "L"]
            new_beam2 = [(x + 1, y), "R"]
            return [new_beam1, new_beam2]
    elif command == "/":
        if d == "U":
            return [[(x + 1, y), "R"]]
        if d == "D":
            return [[(x - 1, y), "L"]]
        if d == "L":
            return [[(x, y + 1), "D"]]
        if d == "R":
            return [[(x, y - 1), "U"]]
    elif command == "\\":
        if d == "D":
            return [[(x + 1, y), "R"]]
        if d == "U":
            return [[(x - 1, y), "L"]]
        if d == "R":
            return [[(x, y + 1), "D"]]
        if d == "L":
            return [[(x, y - 1), "U"]]

    return [[(x,y), d]]


def check_beam(check, e):
    if not(0 <= check[0][0] < len(data[0]) and 0 <= check[0][1] < len(data)):
        return False

    if check[0] not in e.keys():
        return True

    if check[1] in e[check[0]]:
        return False

    return True


def calc_energized(start_queue, direction):
    energized = {}
    queue = []
    queue.append([start_queue, direction])
    while len(queue) > 0:
        beam = queue.pop()

        if beam[0] in energized.keys():
            energized[beam[0]] += beam[1]
        else:
            energized[beam[0]] = beam[1]

        beams = next_beam(beam[0][0], beam[0][1], beam[1])

        for b in beams:
            if check_beam(b, energized):
                queue.append(b)

    return len(energized)


max_energized = 0
for i in range(len(data)):
    max_energized = max(max_energized, calc_energized((0, i), "R"))
    max_energized = max(max_energized, calc_energized((len(data[0])-1, i), "L"))

for i in range(len(data[0])):
    max_energized = max(max_energized, calc_energized((i, 0), "D"))
    max_energized = max(max_energized, calc_energized((i, len(data)-1), "U"))


print(max_energized)



