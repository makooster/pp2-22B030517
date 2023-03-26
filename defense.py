import re
with open("text.txt", 'r') as f:
    x = f.open()
    s = len(f.readline())
def gen(x):
    if s % 2 == 0:
        pattern = r'\D'
        print(re.findall(pattern, x))
g = f.close()
