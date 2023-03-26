def gen():
    i = 1
    while True:
        if i % 2 == 0:
            yield i*i
        i += 1
# print(*gen())
