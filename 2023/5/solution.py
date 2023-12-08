import re

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            content.append(line.rstrip("\n"))

# Solution - part 1

garden_map = {}
seeds = []
for seed in re.findall(r'\d+', content[0]):
    seeds.append(int(seed))

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

locations = []
for idx, seed in enumerate(seeds):
    source = seed
    
    for map, range_idx in garden_map.items():
        dest_map = []
        source_map = []
        destination = source

        for idx, ranges in range_idx.items():
            range_length = ranges['range_length']
            source_start = ranges['source_range_start']
            dest_start = ranges['dest_range_start']
            if source_start <= source < source_start + range_length:
                destination = source - source_start + dest_start
        source = destination
    locations.append(destination)

print(min(locations))

# Solution - part 2
seed_start = seeds[::2]
seed_end = seeds[1::2]
seeds_extended = []
for start, end in zip(seed_start, seed_end):
    seeds_extended.extend(list(range(start, start + end)))

locations = []
for idx, seed in enumerate(seeds_extended):
    source = seed
    
    for map, range_idx in garden_map.items():
        dest_map = []
        source_map = []
        destination = source

        for idx, ranges in range_idx.items():
            range_length = ranges['range_length']
            source_start = ranges['source_range_start']
            dest_start = ranges['dest_range_start']
            if source_start <= source < source_start + range_length:
                destination = source - source_start + dest_start
        source = destination
    locations.append(destination)

print(min(locations))