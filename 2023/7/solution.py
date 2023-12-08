# Read input file as list of strings, remove "\n"
input = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            line = line.rstrip("\n")
            line = line.split()
            input.append(line)

print(input)

# Solution - part 1
input = [
    ['32T3K', '765'],
    ['T55J5', '684'],
    ['KK677', '28'],
    ['KTJJT', '220'],
    ['QQQJA', '483'],
]

