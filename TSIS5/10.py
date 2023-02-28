import re
def cameltosnake(text):
    res = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res