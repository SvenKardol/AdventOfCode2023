from aocd import get_data
dataRaw = get_data(year=2023, day=4)

data = dataRaw.split("\n")
total = 0
for line in data:

    winning = [int(d) for d in line.split(":")[1].strip().split("|")[0].strip().split(" ") if d != ""]
    ours = [int(d) for d in line.split(":")[1].strip().split("|")[1].strip().split(" ") if d != ""]

    start = -1
    for i in ours:
        if i in winning:
            start += 1

    if start > -1:
        total += 2**start

print(total)
