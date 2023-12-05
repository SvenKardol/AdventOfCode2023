from aocd import get_data
dataRaw = get_data(year=2023, day=1)

data = dataRaw.split("\n")

sum = 0
for line in data:
    test = [int(s) for s in line if s.isdigit()]
    value = test[0]*10+test[-1]
    sum+= value

print(sum)