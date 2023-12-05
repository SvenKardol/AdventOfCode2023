from aocd import get_data
dataRaw = get_data(year=2023, day=2)

data = dataRaw.split("\n")

total = 0
for line in data:
    games = line.split(":")[1].split(";")

    red, green, blue = 0, 0, 0
    for g in games:
        colors = g.split(",")

        for c in colors:
            color = c.strip().split(" ")[1]
            amount = int(c.strip().split(" ")[0])

            match color:
                case "red":
                    if amount > red:
                        red = amount
                case "green":
                    if amount > green:
                        green = amount
                case "blue":
                    if amount > blue:
                        blue = amount

    total += (red*green*blue)

print(total)