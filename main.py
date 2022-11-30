import numpy as np

grid = [[1,11,111],[2,22,222],[3,33,333]]
print(grid)

#print(grid[2][1])

print(iter(grid))
           
for i in iter(grid):
    for j in iter(i):
        for k in iter(j):
            if i < i+1:
                i=0
            elif i > i+1:
                i+1
            elif i == i:
                next(i)
    