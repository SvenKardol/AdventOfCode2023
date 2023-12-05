from aocd import get_data
import re as re
import numpy as np

dataRaw = get_data(year=2023, day=1)

data = dataRaw.split("\n")
# data =  "two1nine::eightwothree::abcone2threexyz::xtwone3four::4nineeightseven2::zoneight234::7pqrstsixteen".split("::")
# data =  "onetwothreetwo".split("::")
dict = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0

def sort_list(input):
    output = input
    if len(input) > 0:
        sub_arr = np.array(input)
        indices = sub_arr[:, 1]
        sorted_arr = sub_arr[indices.argsort()]
        output = sorted_arr.tolist()
    return output


for line in data:
    # prevent double digits from wrongly indexing by looping over the length of the line.
    digit = [[int(line[i]), i] for i in range(len(line)) if line[i].isdigit()]

    text = []
    for s in dict:
        # indices = list(find_all(line, s))
        indices = [m.start() for m in re.finditer(s, line)]
        for i in indices:
            text.append([dict.index(s) + 1, i])

    # sorting the list on index digit
    text = sort_list(text)

    val1 = digit[0][0] if len(digit) > 0 else text[0][0]
    val2 = digit[-1][0] if len(digit) > 0 else text[-1][0]

    if len(text) > 0 and len(digit) > 0 and text[0][1] < digit[0][1]:
        val1 = text[0][0]
    if len(text) > 0 and len(digit) > 0 and text[-1][1] > digit[-1][1]:
        val2 = text[-1][0]

    sum += (val1 * 10 + val2)

print(sum)
