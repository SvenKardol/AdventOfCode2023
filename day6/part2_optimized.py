from aocd import get_data

dataRaw = get_data(year=2023, day=6)

data = dataRaw.split("\n")

time = int(data[0].split(":")[1].replace(" ", ""))
dis = int(data[1].split(":")[1].replace(" ", ""))

edge = 0
for t in range(time + 1):
    distance = (time - t) * t
    if distance > dis:
        edge = t
        break

print(time + 1 - 2 * edge)