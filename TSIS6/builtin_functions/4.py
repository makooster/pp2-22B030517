import time

def squarerootAftertime(n, ms):
    # print(time.time())
    time.sleep(ms/1000)
    print(f"Square root of {n} after {ms} milliseconds is {(n)**0.5}")
    print(time.time())
squarerootAftertime(int(input()), int(input()))