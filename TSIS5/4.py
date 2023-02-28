import re

txt = "abbbbbb abb abbbb"

# pattern = r'[A-Z]+[a-z]*'
pattern = r'[A-Z]?[a-z].'

print(re.search(pattern, txt))
