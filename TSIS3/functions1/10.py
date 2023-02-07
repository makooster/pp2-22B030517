def uniquee(l):
    unique_list = []
    for i in l:
        if i  not in unique_list:
            unique_list.append(i)
    print(unique_list)
uniquee(list(map(int, input().split())))