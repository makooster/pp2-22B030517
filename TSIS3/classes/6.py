def filter_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
num = list(map(int, input().split()))

prime_numbers = list(filter(lambda x: filter_prime(x), num))
print("Prime numbers in the list:", prime_numbers)