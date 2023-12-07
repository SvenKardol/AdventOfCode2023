import math

from aocd import get_data
import numpy as np

dataRaw = get_data(year=2023, day=6)

data = dataRaw.split("\n")

# 31 bit
data[0] = "Time:               6074001000"
data[1] = "Distance:  9223372036854775807"

# 31 bit
data[0] = "Time:               2878053387"
data[1] = "Distance:  1661589816380250885"

# 63 bit
data[0] = "Time:                        16107645505445695488"
data[1] = "Distance:  64856007359523503909674096462042349751"

time = int(data[0].split(":")[1].replace(" ", ""))
dis = int(data[1].split(":")[1].replace(" ", ""))


#               /|
#              / |
#             /  |     (time-t)t
#____________/___|
#      t    time-t
# distance = (time-t)t

# d = tx -x2
# x^2 - tx + d = 0

coeff = [1, -time, dis]
roots = np.roots(coeff)
roots.sort()

print(int(math.floor(roots[1])-math.ceil(roots[0])), int(math.floor(roots[1])-math.ceil(roots[0])) % 1000)
