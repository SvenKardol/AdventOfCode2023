from aocd import get_data

dataRaw = get_data(year=2023, day=9)

data = dataRaw.split("\n")


def determine_diff_set(nums):
    return_set = [nums]
    while True:
        diff = [return_set[-1][i + 1] - return_set[-1][i] for i in range(len(return_set[-1]) - 1)]
        return_set.append(diff)

        if all([v == 0 for v in diff]):
            break

    return return_set


total = 0
for line in data:
    original_nums = [int(num) for num in line.split()]

    diff_set = determine_diff_set(original_nums)

    while len(diff_set) > 1:
        sequence_increment = diff_set[-1][-1]
        diff_set.remove(diff_set[-1])

        # append found value to the last diff_set
        diff_set[-1].append(diff_set[-1][-1] + sequence_increment)

    # add last element of each set to the total
    total += diff_set[0][-1]

print(total)
