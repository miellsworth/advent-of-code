import re

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line.rstrip("\n"))

# Solution - part 1

cards = {}
for idx, line in enumerate(content):
    numbers = re.findall(r'\d+', line)
    cards[idx + 1] = {
        'winning_num': numbers[1:11],
        'my_num': numbers[11:36],
    }

for card_num, card in cards.items():
    matches = 0
    for number in card['my_num']:
        if number in card['winning_num']:
            matches += 1
            card['matches'] = matches
            card['points'] = 2 ** (matches - 1)

points = 0
for card_num, card in cards.items():
    if 'points' in card:
        points += card['points']

print(points)

# Solution - part 2
for card_num, card in cards.items():
    card_matches = []
    card['cards'] = card_matches
    if 'matches' in card:
        card_matches = [i for i in range(card_num + 1, card_num + card['matches'] + 1)]
        card['cards'] = card_matches