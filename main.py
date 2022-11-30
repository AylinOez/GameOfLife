import numpy as np

grid = [[0,1,0], [0,1,0],[0,1,0]]
print(grid)

for i in range(3):
    for j in range(3):
        neighborlist= []
        neighborlist.append(len(str(i)))
        neighborlist.append(len(str(j)))
        print(neighborlist)