#read file into 2d array

with open('d4puzzle.txt', 'r') as file:
    twodlist = [list(line.rstrip()) for line in file]
    print(twodlist)

#loop through every letter

directions = [[1,0],[1,1],[0,1],[-1,0],[-1,-1],[-1,1],[1,-1],[0,-1]]
xmassesFound = 0

for rowidx, row in enumerate(twodlist):
    #print(row)
    for colidx,firstchar in enumerate(row):
        #print(firstchar)

        #is it X?
        if firstchar == "X":
            print("X")
            #loop through all 8 directions
            #are the 3 in that direction M,A,S? If so, add+1
            for direction in directions:
                try:
                    if twodlist[rowidx+direction[0]][colidx+direction[1]] == "M":
                        if twodlist[rowidx+(direction[0]*2)][colidx+(direction[1]*2)] == "A":
                            if twodlist[rowidx+(direction[0]*3)][colidx+(direction[1]*3)] == "S":
                                if rowidx+(direction[0]*3) >=0 and colidx+(direction[1]*3) >=0:  #hasnt overflowed. count it.
                                    print("FOUND ONE! YIPPEE!" + str(direction))
                                    #print(direction)
                                    xmassesFound += 1
                except:
                    foo = "bar"

print(xmassesFound)