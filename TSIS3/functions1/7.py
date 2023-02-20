def has_33(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i == int('3') and j == int('3'):
                return True
            else:
                return False
print(has_33(list(map(int, input().split()))))
