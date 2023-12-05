from aocd import get_data
from collections import defaultdict

dataRaw = get_data(year=2023, day=4)

data = dataRaw.split("\n")

total = 0
cards_won = defaultdict()

for i in range(len(data)):
    cards_won[i + 1] = 1

for card in cards_won:
    total += cards_won[card]
    line = data[card-1]
    card_id = [int(d) for d in line.split(":")[0].strip().split(" ") if d.isdigit()][0]

    winning = [int(d) for d in line.split(":")[1].strip().split("|")[0].strip().split(" ") if d != ""]
    ours = [int(d) for d in line.split(":")[1].strip().split("|")[1].strip().split(" ") if d != ""]

    start = 0
    for i in ours:
        if i in winning:
            start += 1

    for i in range(1, start + 1):
        cards_won[card_id + i] += cards_won[card]

print(total)
