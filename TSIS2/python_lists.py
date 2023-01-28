thislist = ["apple", "banana", "cherry"]
print(thislist)
#changeable
#dublicates are allowed
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#ordered
#list's length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#examples of lists
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#lists can contain different data types
list1 = ["abc", 34, True, 40, "male"]
#defining the list's class type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#constructing lists using list()function
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

"""ACCESS LIST ITEMS"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#range of indices
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#also range from the beginning 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#range till the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#range of negative indices
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#checking the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

"""CHANGE LIST ITEMS"""
#changing the item 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#changing using the range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#replacing one item with more ones
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#replacing two items with one
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#insertinig the items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

"""ADD LIST ITEMS"""
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

"""REMOVE LIST ITEMS"""
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

""" LOOP LISTS"""
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""LIST COMPREHENSION"""
#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
#With no if statement:
newlist = [x for x in fruits]
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

"""SORT LISTS"""
#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

"""COPY LISTS"""
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

"""JOIN LISTS"""
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""LIST EXERCISES"""
#1 
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))