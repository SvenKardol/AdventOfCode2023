from aocd import get_data
dataRaw = get_data(year=2023, day=7)

data = dataRaw.split("\n")

cards = []
scored_cards = []
values = list("AKQT98765432J"[::1])

# read data
for line in data:
    card = [line.split()[0], int(line.split()[1])]
    cards.append(card)


# replace the J in the string with the highest counted letter
# with a tie doesn't matter which you replace, since scores are not dependent on which letter has the highest count.
def replace_joker(c):
    if "J" not in c:
        return c

    string_no_joker = c.replace("J", "")
    if len(string_no_joker) == 0:
        return c

    char_dict = count_letters(string_no_joker)
    char = max(char_dict, key=char_dict.get)

    return c.replace("J", char)


# count the letters in a card and create a dictionary of it.
def count_letters(s):
    char_count = {}

    for char in s:
        if char.isalpha() or (char.isdigit() and len(char) == 1):
            char_count[char] = char_count.get(char, 0) + 1

    return char_count


# card value: highest value for highest letter
# jumps are per 100 instead of 10, because there are more than 10 letter values
# 1st char   : 1e8 * value letter
# 2nd char   : 1e6 * value letter
# 3rd char   : 1e4 * value letter
# 4th char   : 1e2 * value letter
# 5th char   : 1e0 * value letter
def get_card_value(c):
    index = (len(values) - values.index(c[0][0])) * 1E8
    index += (len(values) - values.index(c[0][1])) * 1E6
    index += (len(values) - values.index(c[0][2])) * 1E4
    index += (len(values) - values.index(c[0][3])) * 1E2
    index += (len(values) - values.index(c[0][4])) * 1E0
    score = index
    return score


# score is defined by what type of hand plus the value of the string you started with to break ties.
# 5 of a kind: score 1e14
# 4 of a kind: score 1e13
# full house : score 2e12
# 3 of a kind: score 1e11
# pair       : score 1e10 per pair
def get_hand_score(char_dict):
    score = 0
    for letter, count in char_dict.items():
        # 5 of a kind
        if len(char_dict) == 1:
            score += 1E14

        # full house or 4 of a kind
        elif len(char_dict) == 2:
            if count == 4:
                score += 1E13

            if count == 3 or count == 2:
                score += 1E12

        else:
            # three of a kind
            if count == 3:
                score += 1E11

            # pair(s)
            if count == 2:
                score += 1E10
    return score


# get score.
# score = card_value + hand_value
def get_score(c):
    score = get_card_value(c)

    char_dict = count_letters(replace_joker(c[0]))
    score += get_hand_score(char_dict)

    return [score, c[1]]


for card in cards:
    scored_cards.append(get_score(card))

sorted_scored_cards = sorted(scored_cards, key=lambda x: x[0])

total = 0
for i in range(len(sorted_scored_cards)):
    total += (i + 1) * sorted_scored_cards[i][1]

print(total)

