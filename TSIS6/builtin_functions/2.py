def cnt(inp):
    
    Upper_case = 0
    Lower_case = 0

    for i in inp:
        if i.isupper():
            Upper_case += 1
        elif i.islower():
            Lower_case += 1
    print(inp)
    print(f"The num of uppercase letters : {Upper_case}")
    print(f"The num of lowercase letters : {Lower_case}")


cnt(input())      