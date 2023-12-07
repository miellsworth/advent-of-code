import re

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            content.append(line.rstrip("\n"))

# Solution - part 1

garden_map = {}
garden_map['seeds'] = re.findall(r'\d+', content[0])
seeds_int = []
for seed in garden_map['seeds']:
    seeds_int.append(int(seed))

garden_map['seeds'] = seeds_int

def create_garden_map(garden_map, source_dest, content_list):
    garden_map[source_dest] = {}
    for idx, line in enumerate(content_list):
        ranges = re.findall(r'\d+', line)
        range_dict = {}
        range_dict['dest_range_start'] = int(ranges[0])
        range_dict['source_range_start'] = int(ranges[1])
        range_dict['range_length'] = int(ranges[2])
        garden_map[source_dest][idx] = range_dict
    return garden_map

garden_map = create_garden_map(garden_map, 'seed_soil', content[2:45])
garden_map = create_garden_map(garden_map, 'soil_fertilizer', content[46:77])
garden_map = create_garden_map(garden_map, 'fertilizer_water', content[78:103])
garden_map = create_garden_map(garden_map, 'water_light', content[104:131])
garden_map = create_garden_map(garden_map, 'light_temp', content[132:160])
garden_map = create_garden_map(garden_map, 'temp_humidity', content[161:199])
garden_map = create_garden_map(garden_map, 'humidity_location', content[200:249])

# Sample input
seeds = [79, 14, 55, 13]
garden_map = {
    'seed_soil': {
        0: {
            'dest_range_start': 50,
            'source_range_start': 98,
            'range_length': 2
        },
        1: {
            'dest_range_start': 52,
            'source_range_start': 50,
            'range_length': 48
        }
    },
    'soil_fertilizer': {
        0: {
            'dest_range_start': 0,
            'source_range_start': 15,
            'range_length': 37
        },
        1: {
            'dest_range_start': 37,
            'source_range_start': 52,
            'range_length': 2
        },
        2: {
            'dest_range_start': 39,
            'source_range_start': 0,
            'range_length': 15
        }  
    },
    'fertilizer_water': {
        0: {
            'dest_range_start': 49,
            'source_range_start': 53,
            'range_length': 8
        },
        1: {
            'dest_range_start': 0,
            'source_range_start': 11,
            'range_length': 42
        },
        2: {
            'dest_range_start': 42,
            'source_range_start': 0,
            'range_length': 7
        },
        3: {
            'dest_range_start': 57,
            'source_range_start': 7,
            'range_length': 4
        },
    },
    'water_light': {
        0: {
            'dest_range_start': 88,
            'source_range_start': 18,
            'range_length': 7
        },
        1: {
            'dest_range_start': 18,
            'source_range_start': 25,
            'range_length': 70
        },
    },
    'light_temp': {
        0: {
            'dest_range_start': 45,
            'source_range_start': 77,
            'range_length': 23
        },
        1: {
            'dest_range_start': 81,
            'source_range_start': 45,
            'range_length': 19
        },
        2: {
            'dest_range_start': 68,
            'source_range_start': 64,
            'range_length': 13
        },
    },
    'temp_humidity': {
        0: {
            'dest_range_start': 0,
            'source_range_start': 69,
            'range_length': 1
        },
        1: {
            'dest_range_start': 1,
            'source_range_start': 0,
            'range_length': 69
        },
    },
    'humidity_location': {
        0: {
            'dest_range_start': 60,
            'source_range_start': 56,
            'range_length': 37
        },
        1: {
            'dest_range_start': 56,
            'source_range_start': 93,
            'range_length': 4
        },
    },
}

# for seed in seeds:
locations = []
dest_map = []
source_map = []
for idx, ranges in garden_map['seed_soil'].items():
    range_length = ranges['range_length']
    source_start = ranges['source_range_start']
    dest_start = ranges['dest_range_start']
    source_map.extend(list(range(source_start, source_start + range_length)))
    dest_map.extend(list(range(dest_start, dest_start + range_length)))

seed = seeds[0]
if seed in source_map:
    index = source_map.index(seed)
    destination = dest_map[index]
else:
    destination = seed

print(destination)