def histogram(l):
    ll = []
    for i in range(len(l)):
        ll.append('*' * l[i])
    return ll 
print(histogram(list(map(int, input().split()))))
    