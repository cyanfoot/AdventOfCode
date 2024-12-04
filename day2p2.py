with open("AdventOfCode2024/2ndPuzz.txt",'r') as file:

    numSafe = 0
    print("bar")
    for line in file:
        
        report = line.split(" ") 
        print(report)   
        reportSafe = False
        for j in range(len(report)): #runs for each one as damper
            dampedreport = report.copy()
            dampedreport.pop(j)
            print(dampedreport)
            safe = True
            #check increase
            increasing = False
            decreasing = False
            for i in range(len(dampedreport)-1):
                if int(dampedreport[i]) < int(dampedreport[i+1]) and int(dampedreport[i]) >= (int(dampedreport[i+1])-3):
                    increasing = True
                elif int(dampedreport[i]) > int(dampedreport[i+1]) and int(dampedreport[i]) <= (int(dampedreport[i+1])+3):
                    decreasing = True
                else:
                    safe = False
            if increasing == decreasing:
                safe = False
            print(safe)
            print(increasing)
            print(decreasing)
            print("foo")
            if safe:
                reportSafe = True
        if reportSafe:
            numSafe += 1
print(numSafe)