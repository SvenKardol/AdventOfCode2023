from aocd import get_data

dataRaw = get_data(year=2023, day=13)

data = dataRaw.split("\n\n")


def find_reflection(lines):
    for i in range(1, len(lines[0])):
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


total = 0
for b in data:
    block = b.split("\n")
    vertical_reflection = find_reflection(block)
    if vertical_reflection != -1:
        total += 1 * vertical_reflection
        continue

    block = list(map(''.join, zip(*block)))
    horizontal_reflection = find_reflection(block)
    if horizontal_reflection != -1:
        total += 100 * horizontal_reflection
        continue

print(total)
