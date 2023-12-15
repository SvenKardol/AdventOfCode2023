from aocd import get_data

dataRaw = get_data(year=2023, day=15)

data = dataRaw.replace("\n", "")
# data = "HASH"
# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
print(data)

total = 0

for x in data.split(","):
    subtotal = 0
    for y in x:
        subtotal += ord(y)
        subtotal *= 17
        subtotal = subtotal % 256

    total += subtotal
    print(x, subtotal)

print(total)
