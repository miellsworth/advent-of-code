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

test_seed = garden_map['seeds'][0]
print(test_seed)

index_map = 24
test_seed_soil_map = garden_map['seed_soil'][index_map]
print(test_seed_soil_map)

start = test_seed_soil_map['source_range_start']
end = test_seed_soil_map['source_range_start'] + test_seed_soil_map['range_length']
print(start)
print(end)


if start <= test_seed <= end:
    print('yes')