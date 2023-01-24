print("Hello")
print('Hello')

a = "Hello"
print(a)

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#similar to the upper one
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#strings as arrays of characters
a = "Hello, World!"
print(a[1])
#loops for strings
for x in "banana":
  print(x)
#the way to count the length of the word
a = "Hello, World!"
print(len(a))
#checking a word or character in the string
txt = "The best things in life are free!"
print("free" in txt) #function "in"

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#checking if not
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#to get characters in one range
b = "Hello, World!"
print(b[2:5])
#slice from the start
b = "Hello, World!"
print(b[:5])
#slice to the end
b = "Hello, World!"
print(b[2:])
#slicing from the end using negative positions
b = "Hello, World!"
print(b[-5:-2])
#upper case
a = "Hello, World!"
print(a.upper())
#lower case
a = "Hello, World!"
print(a.lower())
#removing whitespaces from two sides :: function "strip"
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#replace
a = "Hello, World!"
print(a.replace("H", "J"))
#string split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#merging strings as variables
a = "Hello"
b = "World"
c = a + b
print(c)
#adding a space between variables
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#inserting numbers into strings using "format" function
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#it is unlimited in point of variables
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#probability of using exact numbers to use format 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#escaping characters using double quotes
txt = "We are the so-called \"Vikings\" from the north."

"""
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H","J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""