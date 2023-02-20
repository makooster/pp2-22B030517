def gen(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i
        i += 1
print(*gen(int(input())))