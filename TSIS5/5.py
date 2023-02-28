import re

txt = "abbbbbb abb abbbb"

pattern = r'a.*b'

print(re.search(pattern, txt))
