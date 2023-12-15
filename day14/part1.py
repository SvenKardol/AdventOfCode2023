from aocd import get_data
dataRaw = get_data(year=2023, day=14)

# dataRaw = "O....#....:O.OO#....#:.....##...:OO.#O....O:.O.....O#.:O.#..O.#.#:..O..#O..O:.......O..:#....###..:#OO..#....".replace(":", "\n")
data = dataRaw.split("\n")

blocked = set()


def find_cubes():
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "#":
                blocked.add((x, y))


find_cubes()

total_leverage = 0
leverage = len(data)
for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch != "O":
            continue
        pos = (x, y)
        while True:
            if pos in blocked or pos[0] < 0 or pos[1] < 0:
                blocked.add((pos[0], pos[1]+1))
                total_leverage += leverage - pos[1] - 1
                break
            else:
                pos = (x, pos[1] - 1)

print(total_leverage)



