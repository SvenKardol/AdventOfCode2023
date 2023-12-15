from aocd import get_data

dataRaw = get_data(year=2023, day=15)
data = dataRaw.replace("\n", "")


def get_box_nr(c):
    box = 0
    for y in c:
        if y == "-" or y == "=":
            break
        box += ord(y)
        box *= 17
        box = box % 256
    return box


def update_boxes(box_dict, x):
    box_nr = get_box_nr(x)

    if box_nr not in box_dict.keys():
        box_dict[box_nr] = {}

    if "-" in x:
        code = x.split("-")[0]
        if code in box_dict[box_nr]:
            box_dict[box_nr].pop(code)
    else:
        code = x.split("=")[0]
        focal_length = int(x.split("=")[1])
        box_dict[box_nr][code] = focal_length

    return box_dict


def score(box_dict):
    total = 0
    for box in box_dict.keys():
        i = 1
        for lens in box_dict[box].values():
            total += (box + 1) * i * int(lens)
            i += 1
    return total


def part2():
    boxes = {}
    for l in data.split(","):
        boxes = update_boxes(boxes, l)
    return boxes


part2()

print(score(part2()))
