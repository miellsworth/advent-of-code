import re
import math

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line.rstrip("\n"))

# Solution - part 1

integers_with_positions = {}
for idx, line in enumerate(content):
    integers_with_positions[idx] = [
        {
            'integer': int(match.group()),
            'start': match.start() - 1,
            'end': match.end()
        } for match in re.finditer(r'\d+', line)
    ]

symbols_with_positions = {}
first_line = content[0]
second_line = content[1]
last_line = content[-1]
second_last_line = content[-2]

symbols_with_positions[0] = [
    {
        'symbol': str(match.group()),
        'position': match.start(),
    } for match in re.finditer(r'[^a-zA-Z0-9.]', first_line)
]
symbols_with_positions[0].extend([
    {
        'symbol': str(match.group()),
        'position': match.start(),
    } for match in re.finditer(r'[^a-zA-Z0-9.]', second_line)
])

for idx in range(1, len(content) - 1):
    symbols_with_positions[idx] = [
        {
            'symbol': str(match.group()),
            'position': match.start(),
        } for match in re.finditer(r'[^a-zA-Z0-9.]', content[idx])
    ]
    symbols_with_positions[idx].extend([
        {
            'symbol': str(match.group()),
            'position': match.start(),
        } for match in re.finditer(r'[^a-zA-Z0-9.]', content[idx - 1])
    ])
    symbols_with_positions[idx].extend([
        {
            'symbol': str(match.group()),
            'position': match.start(),
        } for match in re.finditer(r'[^a-zA-Z0-9.]', content[idx + 1])
    ])

symbols_with_positions[len(content) - 1] = [
    {
        'symbol': str(match.group()),
        'position': match.start(),
    } for match in re.finditer(r'[^a-zA-Z0-9.]', last_line)
]
symbols_with_positions[len(content) - 1].extend([
    {
        'symbol': str(match.group()),
        'position': match.start(),
    } for match in re.finditer(r'[^a-zA-Z0-9.]', second_last_line)
])

print(integers_with_positions[0])
print(symbols_with_positions[0])
adjacent_ints = []
for int_line_num, integer_details in integers_with_positions.items():
    for integer in integer_details:
         for symbol in symbols_with_positions[int_line_num]:
            if integer['start'] <= symbol['position'] <= integer['end']:
                adjacent_ints.append(integer['integer'])
                break

print(sum(adjacent_ints))

# Solution - part 2
symbols_with_positions = {}
for idx, line in enumerate(content):
    symbols_with_positions[idx] = [
        {
            'symbol': str(match.group()),
            'position': match.start(),
        } for match in re.finditer(r'\*', line)
    ]

integers_with_positions = {}
integers_with_positions[0] = [
    {
        'integer': int(match.group()),
        'start': match.start() - 1,
        'end': match.end()
    } for match in re.finditer(r'\d+', first_line)
]
integers_with_positions[0].extend([
    {
        'integer': int(match.group()),
        'start': match.start() - 1,
        'end': match.end()
    } for match in re.finditer(r'\d+', second_line)
])

for idx in range(1, len(content) - 1):
    integers_with_positions[idx] = [
        {
            'integer': int(match.group()),
            'start': match.start() - 1,
            'end': match.end()
        } for match in re.finditer(r'\d+', content[idx])
    ]
    integers_with_positions[idx].extend([
        {
            'integer': int(match.group()),
            'start': match.start() - 1,
            'end': match.end()
        } for match in re.finditer(r'\d+', content[idx - 1])
    ])
    integers_with_positions[idx].extend([
        {
            'integer': int(match.group()),
            'start': match.start() - 1,
            'end': match.end()
        } for match in re.finditer(r'\d+', content[idx + 1])
    ])

integers_with_positions[len(content) - 1] = [
    {
        'integer': int(match.group()),
        'start': match.start() - 1,
        'end': match.end()
    } for match in re.finditer(r'\d+', second_last_line)
]
integers_with_positions[len(content) - 1].extend([
    {
        'integer': int(match.group()),
        'start': match.start() - 1,
        'end': match.end()
    } for match in re.finditer(r'\d+', last_line)
])

adjacent_ints = {}
symbol_count = 0
for sym_line_num, sym_details in symbols_with_positions.items():
    if sym_details:
        for symbol in sym_details:
            symbol_count += 1
            symbol_ints = []
            for integer in integers_with_positions[sym_line_num]:
                if integer['start'] <= symbol['position'] <= integer['end']:
                    symbol_ints.append(integer['integer'])
            adjacent_ints[symbol_count] = symbol_ints

two_adjacent_ints = []
for star, ints in adjacent_ints.items():
    if len(ints) == 2:
        two_adjacent_ints.append(math.prod(ints))

print(sum(two_adjacent_ints))