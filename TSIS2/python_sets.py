'''
A set is a collection which is unordered, unchangeable*, and unindexed.
'''
"""PYTHON SETS"""
#creating sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
#dublicates are not allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#getting the number of items the set
thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 
#different data types in sets
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#different data types in one set
set1 = {"abc", 34, True, 40, "male"}
#defining the data type of the set
myset = {"apple", "banana", "cherry"}
print(type(myset))
#set() constructor to create a set
myset = {"apple", "banana", "cherry"}
print(type(myset))
"""ACCESS SET ITEMS"""
#looping throughout the set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#checking items to existence
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#changing set items
#Once a set is created, you cannot change its items, but you can add new items
"""ADD SET ITEMS"""
#adding via add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#addding from the set to another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#adding elements of lists/tuples/sets
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#removing items using remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#removing items using discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#removing a random item using pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#deleting all the things using clear() methods
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#deleting the set completely
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
"""LOOP SETS"""
#printing all set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
"""JOIN SETS"""
#joining two sets using union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#inserting items of one set and joining it to another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#keeping only the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#intersection() will return a new set containing common items in two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#symmetric_difference() will keep a set containing items that are not common to two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
"""SET EXERCISES"""
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

