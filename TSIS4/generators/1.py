def gen(n):
    for i in range(1, n + 1):
        yield i ** 2
        i += 1
print(*gen(int(input())))
