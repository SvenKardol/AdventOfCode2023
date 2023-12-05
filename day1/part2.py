from aocd import get_data
import re as re
import numpy as np

dataRaw = get_data(year=2023, day=1)

data = dataRaw.split("\n")
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total_sum = 0
for line in data:
    # convert all written digits to one1one, two2two, three3three, etc. This prevents losing letters for other numbers.
    for s in numbers:
        line = line.replace(s, s + str(dict.index(s)+1) + s)

    digits = [int(s) for s in line if s.isdigit()]
    value = digits[0] * 10 + digits[-1]
    total_sum += value

print(total_sum)
