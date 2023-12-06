from aocd import get_data

dataRaw = get_data(year=2023, day=6)

data = dataRaw.split("\n")

time = int(data[0].split(":")[1].replace(" ", ""))
dis = int(data[1].split(":")[1].replace(" ", ""))

better = 0
for t in range(time + 1):
    distance = (time - t) * t
    if distance > dis:
        better += 1

print(better)
