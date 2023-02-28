import re

txt = "abbbbbb ,ab.b ab..bbb"
txt1 = "abbbbbb, abb ,abbbb"
txt2 = "........ksjsj"

pattern = r'[\s.,]'

# print(re.sub("\s", ":", txt))
# print(re.sub(",", ":", txt1))
# print(re.sub("[.]", ":", txt2))
print(re.sub(pattern, ':', txt))