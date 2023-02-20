def gen(n):
    for i in range (n, 0, -1):
        yield i
        i += 1
print(*gen(int(input())))