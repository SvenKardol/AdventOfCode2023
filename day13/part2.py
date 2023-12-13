from aocd import get_data

dataRaw = get_data(year=2023, day=13)
data = dataRaw.split("\n\n")


def find_reflection(lines, avoid):
    for i in range(1, len(lines[0])):
        if i == avoid:
            continue
        diff_to_edge = min(i, len(lines[0]) - i)

        mirrored = True
        for line in lines:
            first_part = line[i - diff_to_edge:i]
            second_part = list(line[i:i + diff_to_edge])
            second_part.reverse()
            second_part = ''.join(second_part)

            if second_part != first_part:
                mirrored = False

        if not mirrored:
            continue
        else:
            return i

    return -1


def find_reflection_xy(b):
    vertical_reflection = find_reflection(b, -1)

    b = list(map(''.join, zip(*b)))
    horizontal_reflection = find_reflection(b, -1)
    return horizontal_reflection, vertical_reflection


def find_reflection_avoid(b, avoid_x, avoid_y):
    vertical_reflection = find_reflection(b, avoid_y)

    b = list(map(''.join, zip(*b)))
    horizontal_reflection = find_reflection(b, avoid_x)
    return horizontal_reflection, vertical_reflection


def score(r, c):
    if r != -1:
        return 100 * r
    return c


total = 0
for b in data:
    block = b.split("\n")
    (orig_x, orig_y) = find_reflection_xy(block)

    found_new_mirror = False
    for y in range(len(block)):
        if found_new_mirror:
            break
        for x in range(len(block[y])):
            temp_block = [item for item in block]
            if block[y][x] == "#":
                temp_block[y] = block[y][:x] + "." + block[y][x + 1:]
            else:
                temp_block[y] = block[y][:x] + "#" + block[y][x + 1:]
            (x_r, y_r) = find_reflection_avoid(temp_block, orig_x, orig_y)
            if x_r != -1 and x_r != orig_x:
                found_new_mirror = True
                total += score(x_r, y_r)
                break
            if y_r != -1 and y_r != orig_y:
                found_new_mirror = True
                total += score(x_r, y_r)
                break

print(total)
