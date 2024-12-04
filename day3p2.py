import re

with open('d3puzzle.txt', 'r') as file:
    total = 0
    data = file.read().replace('\n', '')

    #split
    deDontifiedData = re.sub("(don't\(\).+?do\(\))","💩",data)
    print(deDontifiedData)

    instructions = re.findall("(mul\(\d+,\d+\))",deDontifiedData)

    for instruction in instructions:
        numbers = re.findall("\d+", instruction)
        multiple = int(numbers[0]) * int(numbers[1])
        print(multiple)
        total += multiple
    print(total)
        
