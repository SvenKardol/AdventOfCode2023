from aocd import get_data

dataRaw = get_data(year=2023, day=6)

data = dataRaw.split("\n")

time = [int(t) for t in data[0].split(":")[1].split()]
dis = [int(d) for d in data[1].split(":")[1].split()]

total = 1
for i in range(len(time)):
    print(time[i], dis[i])

    better = 0
    for t in range(time[i] + 1):
        distance = (time[i] - t) * t
        if distance > dis[i]:
            better += 1

    total *= better

print(total)
