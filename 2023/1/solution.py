import re

# Read input file
content = []
with open('input.txt', 'r') as f:
    for line in f:
        content.append(line.rstrip("\n"))

# Solution - part 1

# Define function to extract single digit integers
def extract_numbers_from_string(text):
    numbers = re.findall(r'\d', text)
    return numbers

# Loop through input file and append list with first and second number
numbers_list = []
for string in content:
    numbers = extract_numbers_from_string(string)
    first_number = numbers[0]
    second_number = numbers[-1]
    numbers_list.append([first_number, second_number])

# Concat first and second number strings, convert to int, and add to calibration sum
calibration_sum = 0
for number in numbers_list:
    calibration_sum += int(number[0] + number[1])

print(calibration_sum)

# Solution - part 2

# Create a dictionary to map text number string to corresponding int number string
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

# Loop through input file
calibration_sum = 0
for line in content:
    # Initialize first and second number variables as None to allow for loop breaks
    first_number = None
    second_number = None
    
    # Iterate through characters in string, forwards
    string = ''
    for char in line:
        # Check if current character is a digit
        if char.isdigit():
            first_number = char
            break
        
        # Check if string contains a text number
        string = string + char
        for number in numbers.keys():
            if number in string:
                first_number = numbers[number]
                break

        if first_number:
            break

    # Iterate through characters in string, backwards
    string = ''
    for char in reversed(line):
        # Check if current character is a digit
        if char.isdigit():
            second_number = char
            break

        # Check if string contains a text number
        string = char + string
        for number in numbers.keys():
            if number in string:
                second_number = numbers[number]
                break
        
        if second_number:
            break
    
    # Concat first and second number strings, convert to int, and add to calibration sum
    line_number = int(first_number + second_number)
    calibration_sum += line_number

print(calibration_sum)