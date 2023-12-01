import re

# Part one
def extract_numbers_from_string(text):
    numbers = re.findall(r'\d', text)
    return numbers

content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line.rstrip("\n"))

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

# Part two
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

calibration_sum = 0
first_last_numbers_list = []

for line in content:
    number_list = None
    number_list_2 = None
    string_test = ''
    for string in line:
        if number_list:
            break
        
        string_test = string_test + string
        if string.isdigit():
            number_list = string
            break

        for number in numbers.keys():
            if number in string_test:
                number_list = numbers[number]
                break

    string_test = ''
    for string in reversed(line):
        if number_list_2:
            break
        string_test = string + string_test
        if string.isdigit():
            number_list_2 = string
            break

        for number in numbers.keys():
            if number in string_test:
                number_list_2 = numbers[number]
                break

    line_number = int(number_list + number_list_2)
    calibration_sum += line_number

print(calibration_sum)