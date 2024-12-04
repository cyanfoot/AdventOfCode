#read file into 2d array

with open('d4puzzle.txt', 'r') as file:
    twodlist = [list(line.rstrip()) for line in file]
    print(twodlist)

#loop through every letter

directions = [[1,1],[-1,-1]]
xdashmassesFound = 0

for rowidx, row in enumerate(twodlist):
    #print(row)
    for colidx,firstchar in enumerate(row):
        #print(firstchar)

        #is it X?
        if firstchar == "A":
            print(colidx,rowidx)
            #loop through all 4 directions
            #are the 3 in that direction M,A,S? If so, add+1
            for direction in directions:
                try:
                    if twodlist[rowidx+direction[0]][colidx+direction[1]] == "M" and twodlist[rowidx+(direction[0]*-1)][colidx+(direction[1]*-1)] == "S":
                            if (twodlist[rowidx+(direction[0]*-1)][colidx+(direction[1])] == "M" and twodlist[rowidx+(direction[0])][colidx+(direction[1]*-1)] == "S") or (twodlist[rowidx+(direction[0]*-1)][colidx+(direction[1])] == "S" and twodlist[rowidx+(direction[0])][colidx+(direction[1]*-1)] == "M"):
                                    if rowidx+(direction[0]) >=0 and colidx+(direction[1]) >=0 and rowidx+(direction[0]*-1) >=0 and colidx+(direction[1]*-1) >=0:  #hasnt overflowed. count it.
                                        print("FOUND ONE! YIPPEE!" + str(direction))
                                        #print(direction)
                                        xdashmassesFound += 1
                except:
                    foo = "bar"

print(xdashmassesFound)
