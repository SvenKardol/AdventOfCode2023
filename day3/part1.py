from aocd import get_data
import re
dataRaw = get_data(year=2023, day=3)

data = dataRaw.split("\n")
total = 0


def is_symbol(cx, cy):
    if 0 <= cx < len(data[0]) and 0 <= cy < len(data) and data[cy][cx] != "." and not data[cy][cx].isdigit():
        return True
    return False


for y, line in enumerate(data):
    x = 0
    while x < len(line):
        if line[x].isdigit():
            left_edge = x
            right_edge = x+1

            while right_edge < len(line) and line[right_edge].isdigit():
                right_edge += 1

            num = line[left_edge: right_edge]

            x = right_edge

            add = False
            for cy in range(y-1, y+2):
                for cx in range(left_edge - 1, right_edge + 1):
                    if is_symbol(cx, cy):
                        add = True

            if add:
                total += int(num)


        else:
            x += 1



print(total)


