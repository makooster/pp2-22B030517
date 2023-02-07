from itertools import permutations
def permm(inp):
    perm = permutations(inp)
    for x in perm:
        print(x)
permm(input())
    