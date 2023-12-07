# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            content.append(line.rstrip("\n"))

# Solution - part 1
input = {}
for line in content:
    strings = line.split()
    values = []
    for i in strings[1:5]:
        values.append(int(i))
    input[strings[0].replace(":", "")] = values

race_options = {}
option_counter = {}
for idx, time in enumerate(input['Time']):
    counter = 0
    speed = 0
    distances = {}
    for hold_time in range(time + 1):
        speed = hold_time
        travel_time = time - hold_time
        distance = travel_time * speed
        distances[hold_time] = distance
        if distance > input['Distance'][idx]:
            counter += 1
    race_options[time] = distances
    option_counter[time] = counter

solution = 1
for count in option_counter.values():
    solution = solution * count

print(solution)

# Solution - part 2