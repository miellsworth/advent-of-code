# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            line = line.rstrip("\n")
            line = line.split()
            content.append(line)

input = {}
input['instruction'] = ''.join(content[0])
for idx, line in enumerate(content[1:]):
    left_element = ''.join([char for char in line[2] if char.isalpha()])
    right_element = ''.join([char for char in line[3] if char.isalpha()])
    input[line[0]] = (left_element, right_element)
print(input)

# Solution - part 1
input = {
    'instruction': 'RL',
    'AAA': ('BBB', 'CCC'),
    'BBB': ('DDD', 'EEE'),
    'CCC': ('ZZZ', 'GGG'),
    'DDD': ('DDD', 'DDD'),
    'EEE': ('EEE', 'EEE'),
    'GGG': ('GGG', 'GGG'),
    'ZZZ': ('ZZZ', 'ZZZ')
}