import random 
num = random.randint(1, 20)
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
cnt = 0
while True:
    inp = int(input("Take guess.\n"))
    cnt += 1
    if inp == num:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    elif inp > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low.")
    