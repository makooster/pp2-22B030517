import re

def w_to_upper(text):
    wordd = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,text)
    for i, word in enumerate(words):
        if i != 0:  
            wordd += " " + word
        else:
            wordd += word
    return wordd