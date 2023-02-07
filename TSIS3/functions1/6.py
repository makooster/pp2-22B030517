def word_reverse(s):
    n = len(s)
    cnt = 0
    l = []
    word = ''
    for i in range (0,n + 1):
        if(i == n):
            l.append(word)
        elif(s[i] != ' '):
            word = word + s[i]
        else:
            l.append(word)
            word = ''
    
    word = ''
    for i in range(len(l) - 1, -1, -1):
        word = word + l[i]
        word = word + ' '

    print(word)

word_reverse('We are ready')


    
