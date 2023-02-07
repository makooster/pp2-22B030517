def filter_prime(l):
    res=True
    l2=list()
    for i in range(len(l)):
        res=True
        if l[i]==2:
            l2.append(l[i])
        else:
            for j in range(2,(l[i]//2)+1):
                if l[i]%j==0:
                    res=False
                    break
            if res==True:
                l2.append(l[i])    
    return l2
l=list(map(int,input().split()))
print(filter_prime(l))