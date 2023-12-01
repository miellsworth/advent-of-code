import re

def extract_numbers_from_string(text):
    numbers = re.findall(r'\d', text)
    return numbers

content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line)

numbers_list = []
for string in content:
    numbers_list.append(extract_numbers_from_string(string))

first_last_numbers_list = []
for numbers in numbers_list:
    first_last_numbers_list.append([numbers[0], numbers[-1]])

calibration_sum = 0
for number in first_last_numbers_list:
    calibration_sum += int(number[0] + number[1])

print(calibration_sum)