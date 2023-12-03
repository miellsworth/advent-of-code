import re
import math

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line.rstrip("\n"))

# Solution - part 1

# Define function to extract number from string
def extract_numbers_from_string(text):
    numbers = re.findall(r'\d+', text)
    return numbers

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

game_list = []
for line in content:
    game_list.append(line.split(':'))

game_dict = {}
for game in game_list:
    game_num = int(extract_numbers_from_string(game[0])[0])
    game_info = game[1]
    game_dict[game_num] = game_info.split(';')

detailed_dict = {}
for game, info in game_dict.items():
    info_dict = {}
    for idx, string in enumerate(info):
        col_dict = {}
        red = re.search(r'\d+\sred', string)
        if red:
            red_num = extract_numbers_from_string(red.group(0))
            col_dict['red'] = int(red_num[0])
        
        green = re.search(r'\d+\sgreen', string)
        if green:
            green_num = extract_numbers_from_string(green.group(0))
            col_dict['green'] = int(green_num[0])
        
        blue = re.search(r'\d+\sblue', string)
        if blue:
            blue_num = extract_numbers_from_string(blue.group(0))
            col_dict['blue'] = int(blue_num[0])
        
        info_dict[idx] = col_dict
    detailed_dict[game] = info_dict

possible_games = []
for game, info in detailed_dict.items():
    impossible_info = []
    for info_num, cube_count in info.items():
        for color in cube_count:
            if cube_count[color] > cubes[color]:
                impossible_info.append(info_num)
                break

    if not impossible_info:
        possible_games.append(game)

print(sum(possible_games))

# Solution - part 2
game_min_dict = {}
for game, info, in detailed_dict.items():
    color_count = {'red': [], 'green': [], 'blue': []}
    for info_num, cube_count in info.items():
        for color, color_counts in cube_count.items():
            color_count[color].append(color_counts)
    
    color_min = {'red': 0, 'green': 0, 'blue': 0}
    for color, color_counts in color_count.items():
        color_min[color] = max(color_counts)

    game_min_dict[game] = color_min

power_list = []
for game, color_mins in game_min_dict.items():
    prod = math.prod(color_mins.values())
    power_list.append(prod)

print(sum(power_list))