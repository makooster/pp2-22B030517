import re

txt = "abbb abb abbbb"

pattern = r'ab{2,3}'

print(re.findall(pattern, txt))
