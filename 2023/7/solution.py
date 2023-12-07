# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            content.append(line.rstrip("\n").split())

# Solution - part 1
input = [
    ['32T3K', '765'],
    ['T55J5', '684'],
    ['KK677', '28'],
    ['KTJJT', '220'],
    ['QQQJA', '483'],
]

