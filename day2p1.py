with open("AdventOfCode2024/2ndPuzz.txt",'r') as file:

    numSafe = 0
    print("bar")
    for line in file:
        report = line.split(" ") 
        print(report)   
        safe = True
        #check increase
        increasing = False
        decreasing = False
        for i in range(len(report)-1):
            if int(report[i]) < int(report[i+1]) and int(report[i]) >= (int(report[i+1])-3):
                increasing = True
            elif int(report[i]) > int(report[i+1]) and int(report[i]) <= (int(report[i+1])+3):
                decreasing = True
            else:
                safe = False
        if increasing == decreasing:
            safe = False
        print(safe)
        print(increasing)
        print(decreasing)
        if safe:
            numSafe += 1
        print("foo")
print(numSafe)