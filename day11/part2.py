from aocd import get_data
dataRaw = get_data(year=2023, day=11)
data = dataRaw.split("\n")

empty_rows = [r for r, row in enumerate(data) if '#' not in row]

#transpose data
data = list(map(list, zip(*data)))
empty_cols = [c for c, col in enumerate(data) if '#' not in col]

# transpose back
data = list(map(list, zip(*data)))

galaxies = []
for r, row in enumerate(data):
    for c, character in enumerate(row):
        if character == "#":
            galaxies.append((r, c))


def distance(galaxy1, galaxy2):
    return abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1] - galaxy2[1])


total = 0


def add_extra_rows():
    extra_dis = 0
    r1, r2 = sorted([g1[0], g2[0]])
    for empty_row in empty_rows:
        if r1 < empty_row < r2:
            extra_dis += 1000000 - 1
    return extra_dis


def add_extra_cols():
    extra_dis = 0
    c1, c2 = sorted([g1[1], g2[1]])
    for empty_col in empty_cols:
        if c1 < empty_col < c2:
            extra_dis += 1000000 - 1
    return extra_dis


for i, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies[:i]):
        dis = distance(g1, g2)
        dis += add_extra_rows()
        dis += add_extra_cols()
        total += dis

print(total)

