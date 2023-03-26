import re
with open("text.txt", 'r') as f:
    x = f.open()
pattern = r'\d{3}'
print(re.sub(pattern, '*', x))
g = f.close()