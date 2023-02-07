def solve(numheads, numlegs):
    for x in range(numlegs + 1):
        y = numheads - x
        if x*2 + y*4 == numlegs:
            return x, y
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))