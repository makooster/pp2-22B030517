#printing via for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#for loops in strings
for x in "banana":
  print(x)
#break in for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#break before print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#continue in for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#range()function
for x in range(6):
  print(x)
#with start parameter
for x in range(2, 6):
  print(x)
#configuring steps of iterations
for x in range(2, 30, 3):
  print(x)
#else in for loops
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#if break works first,then else part will be ignored
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#for loops cannot be empty, so we use "pass"function
for x in [0, 1, 2]:
  pass
"""FOR LOOPS EXERCISES"""
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#3
for x in range(6):
  print(x)
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
