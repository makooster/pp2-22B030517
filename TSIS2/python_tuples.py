'''
A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''
"""PYTHON TUPLES"""
#creating a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Also in tuples it is allowed to have dublicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#the number of elements in a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#accessing only one item in a tuple
# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
#data types in tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#tuple with different data type values
tuple1 = ("abc", 34, True, 40, "male")
#definig the data in a tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
"""ACCESS TUPLES"""
#accesing by indices
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#accesing by negative indices
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#accesing by range of indices
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#accesing items from the beginning
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#accesing items till the end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#accesing items with the range of negative indices
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#checking an item in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
"""UPDATING TUPLES"""
#to work with tuples we convert them to th lists
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#adding items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#adding tuples to each other
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#removing items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#deleting the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
"""UNPACK TUPLES"""
#packing tuples
fruits = ("apple", "banana", "cherry")
#unpacking tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#using Asterisk --- *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#one more time
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
"""LOOP TUPLES"""
#looping through the tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#loop throuugh the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#looping via while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
"""JOIN TUPLES"""
#joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#multiple tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
"""TUPLES EXERCISES"""
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
