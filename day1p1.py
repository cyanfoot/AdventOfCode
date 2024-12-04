#load file

leftArr = []
rightArr = []
filelength = 0

with open("AdventOfCode2024/1st/1stPuzzleInput.txt",'r') as file:
    for line in file:
        numbers = line.split("   ")
        leftArr.append(numbers[0])
        rightArr.append(numbers[1].rstrip())
        filelength += 1

print(leftArr)
print(rightArr)
leftArr.sort()
rightArr.sort()
print(leftArr)
print(rightArr)

totediff = 0
for i in range (0, filelength):
    diffmin = int(leftArr[i]) - int(rightArr[i])
    diff = abs(diffmin)
    print(diff)
    totediff += diff

print(totediff)