from collections import Counter
from functools import cache

from aocd import get_data

dataRaw = get_data(year=2023, day=12)
data = dataRaw.split("\n")

@cache
def check_option(s, ar):
    s2 = [s for s in s.split(".") if s != ""]
    if "?" not in s:
        if len(s2) != len(ar):
            return "false"

        for i, arrangement in enumerate(ar):
            if len(s2[i]) != arrangement:
                return "false"
        return "option"
    return "queue"


total = 0
for line in data:
    springs = line.split()[0]
    arrangements = tuple([int(l) for l in line.split()[1].split(",")])

    counted = Counter(springs)

    options = set()
    queue = set()
    queue.add(springs)

    while len(queue) > 0:
        option = queue.pop()

        new_option1 = option.replace("?", ".", 1)
        new_option2 = option.replace("?", "#", 1)

        if check_option(new_option1, arrangements) == "queue":
            queue.add(new_option1)
        elif check_option(new_option1, arrangements) == "option":
            options.add(new_option1)

        if check_option(new_option2, arrangements) == "queue":
            queue.add(new_option2)
        elif check_option(new_option2, arrangements) == "option":
            options.add(new_option2)

    total += len(options)

print(total)
