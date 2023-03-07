import os

inp = input()

if os.access(f"./{inp}", os.F_OK):
    if os.path.exists(f'./{inp}'):
        os.remove(f'./{inp}')
        print(os.getcwd())