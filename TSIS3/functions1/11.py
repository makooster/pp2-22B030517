def palindrome(inp):
    if inp == inp[::-1]:
        return True
    else:
        return False
print(palindrome(input()))