from aocd import get_data
dataRaw = get_data(year=2023, day=5)

data = dataRaw.split("\n")

# dataRaw = "seeds: 79 14 55 13>>>>>>seed-to-soil map:>>>50 98 2>>>52 50 48>>>>>>soil-to-fertilizer map:>>>0 15 37>>>37 52 2>>>39 0 15>>>>>>fertilizer-to-water map:>>>49 53 8>>>0 11 42>>>42 0 7>>>57 7 4>>>>>>water-to-light map:>>>88 18 7>>>18 25 70>>>>>>light-to-temperature map:>>>45 77 23>>>81 45 19>>>68 64 13>>>>>>temperature-to-humidity map:>>>0 69 1>>>1 0 69>>>>>>humidity-to-location map:>>>60 56 37>>>56 93 4"
# data = dataRaw.split(">>>")


def convertNum(num, table):
    for line in table:
        if line[1] <= num <= line[1] + line[2]:
            return line[0] + num - line[1]

    return num


seeds = [int(d) for d in data[0].split("seeds: ")[1].split()]

print(seeds)

dataS2S = dataRaw.split("seed-to-soil map:")[1].split("\n\n")[0].split("\n")
# dataS2S = dataRaw.split("seed-to-soil map:")[1].split(">>>>>>")[0].split(">>>")

s2s = []
for d in dataS2S:
    if d == "":
        continue
    s2s.append([int(s) for s in d.split()])

dataS2F = dataRaw.split("soil-to-fertilizer map:")[1].split("\n\n")[0].split("\n")
# dataS2F = dataRaw.split("soil-to-fertilizer map:")[1].split(">>>>>>")[0].split(">>>")

s2f = []
for d in dataS2F:
    if d == "":
        continue
    s2f.append([int(s) for s in d.split()])

dataF2W = dataRaw.split("fertilizer-to-water map:")[1].split("\n\n")[0].split("\n")
# dataF2W = dataRaw.split("fertilizer-to-water map:")[1].split(">>>>>>")[0].split(">>>")

f2w = []
for d in dataF2W:
    if d == "":
        continue
    f2w.append([int(s) for s in d.split()])

dataw2l = dataRaw.split("water-to-light map:")[1].split("\n\n")[0].split("\n")
# dataw2l = dataRaw.split("water-to-light map:")[1].split(">>>>>>")[0].split(">>>")

w2l = []
for d in dataw2l:
    if d == "":
        continue
    w2l.append([int(s) for s in d.split()])

datal2t= dataRaw.split("light-to-temperature map:")[1].split("\n\n")[0].split("\n")
# datal2t = dataRaw.split("light-to-temperature map:")[1].split(">>>>>>")[0].split(">>>")

l2t = []
for d in datal2t:
    if d == "":
        continue
    l2t.append([int(s) for s in d.split()])

datat2h = dataRaw.split("temperature-to-humidity map:")[1].split("\n\n")[0].split("\n")
# datat2h = dataRaw.split("temperature-to-humidity map:")[1].split(">>>>>>")[0].split(">>>")

t2h = []
for d in datat2h:
    if d == "":
        continue
    t2h.append([int(s) for s in d.split()])


datah2l = dataRaw.split("humidity-to-location map:")[1].split("\n\n")[0].split("\n")
# datah2l = dataRaw.split("humidity-to-location map:")[1].split(">>>>>>")[0].split(">>>")

h2l = []
for d in datah2l:
    if d == "":
        continue
    h2l.append([int(s) for s in d.split()])


least = -1
for s in seeds:
    outcome = s
    outcome = convertNum(outcome, s2s)
    outcome = convertNum(outcome, s2f)
    outcome = convertNum(outcome, f2w)
    outcome = convertNum(outcome, w2l)
    outcome = convertNum(outcome, l2t)
    outcome = convertNum(outcome, t2h)
    outcome = convertNum(outcome, h2l)

    if least == -1 or outcome < least:
        least = outcome

print(least)
