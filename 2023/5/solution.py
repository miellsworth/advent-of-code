import re

# Read input file as list of strings, remove "\n"
content = []
with open('input.txt', 'r') as f:
    for line in f:
        if not line.isspace():
            content.append(line.rstrip("\n"))

garden_map = {}
garden_map['seeds'] = re.findall(r'\d+', content[0])

def create_garden_map(garden_map, source_dest, content_list):
    garden_map[source_dest] = {}
    for idx, line in enumerate(content_list):
        ranges = re.findall(r'\d+', line)
        range_dict = {}
        range_dict['dest_range_start'] = ranges[0]
        range_dict['source_range_start'] = ranges[1]
        range_dict['range_length'] = ranges[2]
        garden_map[source_dest][idx] = range_dict
    return garden_map

garden_map = create_garden_map(garden_map, 'seed_soil', content[2:45])
garden_map = create_garden_map(garden_map, 'soil_fertilizer', content[46:77])
garden_map = create_garden_map(garden_map, 'fertilizer_water', content[78:103])
garden_map = create_garden_map(garden_map, 'water_light', content[104:131])
garden_map = create_garden_map(garden_map, 'light_temp', content[132:160])
garden_map = create_garden_map(garden_map, 'temp_humidity', content[161:199])
garden_map = create_garden_map(garden_map, 'humidity_location', content[200:249])