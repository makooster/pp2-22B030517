numbers = [1, 2, 3, 4, 5, 6]
with open('text3.txt', 'w') as f:
    for i in numbers:
        f.write(f'{i}\n')
f.close()
