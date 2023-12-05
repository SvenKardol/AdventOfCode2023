from aocd import get_data
dataRaw = get_data(year=2023, day=2)


data = dataRaw.split("\n")

total = 0
max_color = {"green": 13, "red": 12, "blue": 14}

for line in data:
    game_id = int(line.split(":")[0].split(" ")[1])
    games = line.split(":")[1].split(";")

    possible = True
    for g in games:
        colors = g.split(",")
        for c in colors:
            color = c.strip().split(" ")[1]
            amount = int(c.strip().split(" ")[0])

            if amount > max_color[color]:
                possible = False

    if possible:
        total += game_id


print(total)