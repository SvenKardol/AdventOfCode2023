from aocd import get_data
from collections import defaultdict
import re
dataRaw = get_data(year=2023, day=3)

data = dataRaw.split("\n")
total = 0
symbols = set()
gear_nums = defaultdict(list)


def is_gear(cx, cy):
    if 0 <= cx < len(data[0]) and 0 <= cy < len(data) and data[cy][cx] != "." and not data[cy][cx].isdigit():
        if data[cy][cx] == "*":
            symbols.add((cx, cy))
            return True
    return False


for y, line in enumerate(data):
    x = 0
    while x < len(line):
        if line[x].isdigit():
            left_side = x
            right_side = x + 1

            while right_side < len(line) and line[right_side].isdigit():
                right_side += 1

            num = line[left_side: right_side]

            x = right_side

            for cy in range(y-1, y+2):
                for cx in range(left_side - 1, right_side + 1):
                    if is_gear(cx, cy):
                        gear_nums[(cx, cy)].append(int(num))
        else:
            x += 1


for nums in gear_nums.values():
    if len(nums) == 2:
        total += nums[0] * nums[1]

print(total)


