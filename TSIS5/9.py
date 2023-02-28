import re

def spaces(txt):
    result = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,txt)
    for i, word in enumerate(words):
        if i != 0:
            result += " " + word
        else:
            result += word
    return result
