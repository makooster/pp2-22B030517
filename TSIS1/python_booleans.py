print(10 > 9)
print(10 == 9)
print(10 < 9)

#comparing
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#to print true or false information
print(bool("Hello"))
print(bool(15))
#the same way
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#everything that is not empty and do not eequal to 0 is "true"
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# (), {}, [], "" ,0, None, false === FALSE
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#creating functions that returns boolean value
def myFunction() :
  return True

print(myFunction()) 
#continue
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#clarifying that an object is a certain data type
x = 200
print(isinstance(x, int))
