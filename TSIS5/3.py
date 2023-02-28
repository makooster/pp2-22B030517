import re

txt = "abbbbbb abb abbbb"

pattern = r'\w[a-z]+[_].+[a-z]'
# pattern = r'[a-z]+[_]+[a-z].*\s'

print(re.search(pattern, txt))
