import re

def SnakeToCamelcase(text):
    modified_word=""
    pattern = r'[_]'
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            modified_word += word.capitalize()
        else: 
            modified_word += word
    return modified_word