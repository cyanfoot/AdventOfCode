import re

with open('d3puzzle.txt', 'r') as file:
    # Read each line in the file
    total = 0
    for line in file:
        # Print each line
        print(line.strip())
        instructions = re.findall("(mul\(\d+,\d+\))",line)
        for instruction in instructions:
            numbers = re.findall("\d+", instruction)
            multiple = int(numbers[0]) * int(numbers[1])
            print(multiple)
            total += multiple
    print(total)
        