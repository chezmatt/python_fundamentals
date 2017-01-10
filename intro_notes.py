''' this is the intro to python for coding dojo notes '''
my_string = "This is a string stored in the my_string variable"
my_num = 5 # an integer stored in a variable
my_tuple = (1,2,3,4,5) # a tuple stored in a variable
# a dictionary stored in a variable
my_dictionary = {'name': 'Michael Choi', 'fave_lang': 'Python', 'level': 'Sensei'}
###############
# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
# create variable called greeting that holds the value of a string
greetings = "Hello Ninja!"
print greetings
# you can use single or double quotes for strings
print 'What is your name?'
# we use raw_input()to get user input and set it to a variable
name = raw_input()
print "How old are you?"
# we can also use input() to get user input
age = input()
# adding of variables to a string to be printed is like this:
print "Your name is", name
print "You are", age, "years old"
# you can also add the variable in between strings just like the above
raw_input("\n\nPress the enter key to exit.")
# the line above would make the app not close or exit out automatically.
'''how to concatinate '''
name = "Zen"
print "My name is", name
name = "Zen"
print "My name is " + name
my_string = 'hello world'
print my_string.capitalize()
# the output would be:
# Hello world
my_string = 'Hello WORLD'
print my_string.lower()
# the output would be:
# hello world
my_string = 'Hello WORLD'
print my_string.swapcase()
# the output would be:
# hELLO world
my_string = 'hello world'
print my_string.upper()
# the output would be:
# HELLO WORLD
<string>.find(<substring>)
my_string = "hello world"
print my_string.find("el")
# the output would be:
# 1
my_string = "hello world"
print my_string.replace("world", "kitty")
# the output would be:
# hello kitty
my_string = "egg, egg, Spam, egg and Spam"
print my_string.replace("egg", "Spam", 2)
# the output would be:
# Spam, Spam, Spam, egg and Spam
# notice that only the first 2 "egg" matches were replaced in the string.
###########
# LISTS
##########
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]
x = [1,2,3,4,5]
x.insert(2,99)
print x
#the output would be [1,2,99,3,4,5]
x = [1,2,3,4,5]
x.remove(3)
print x
#the output would be [1,2,4,5]
x = [1,2,3,4,5]
x.pop()
print x
#the output would be [1,2,3,4]
y = [10,11,12,13,14]
y.pop(1)
print y
#the output would be [10,12,13,14]
x = [99,4,2,5,-3];
x.sort()
print x
#the output would be [-3,2,4,5,99];
x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3]
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5]
my_list = [1, 'Zen', 'hi']
print len(my_list)
# the output would be 3
my_list = [1, 7, 3]
print max(my_list)
# the output would be 7
my_list = [1, 7, 3]
print min(my_list)
# the output would be 1
my_list = [0, 'hi', '']
print any(my_list)
# the output would be True since a string would equate to true in this case
my_list = [0, '']
print any(my_list)
# the output would be False since 0 (zero) and an empty string will both be false
my_list = [0, 'Zen', '']
print all(my_list)
# the output would be False
my_list = [4, 'hi']
print all(my_list)
# the output would be True
names = ['KB', 'Oliver', 'Mikey', 'John', 'Michael']
print '\n'.join(names)

for val in "string":
  if val == "i":
    break
  print(val)

for val in "string":
    if val == "i":
    continue
  print(val)

x = 3
y = x
while y > 0:
  print y
  y = y - 1
else:
  print "Final else statement"

x = 3
y = x
while y > 0:
  print y
  y = y - 1
  if y == 0:
    break
else:
 print "Final else statement"
### print all numbers in a range
 for x in range(0, 101):
    if (x % 2 == 0):
        print x
## what is lambda?
g = lambda x: x**2

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
# >>> [18, 9, 24, 12, 27]

print map(lambda x: x * 2 + 10, foo)

#>>> [14, 46, 28, 54, 44, 58, 26, 34, 64]
print reduce(lambda x, y: x + y, foo)
#>>>[14, 46, 28, 54, 44, 58, 26, 34, 64]
#>>>139

def add(a,b):
  x = a + b
  return x
# the return value gets assigned to the "result" variable
result = add(3,5)
print result # this should print 8

A new built-in function, enumerate(), will make certain loops a bit clearer. enumerate(thing), where thing is either an iterator or a sequence, returns a iterator that will return (0, thing[0]), (1, thing[1]), (2, thing[2]), and so forth.

# A common idiom to change every element of a list looks like this:

for i in range(len(L)):
    item = L[i]
    # ... compute some result based on item ...
    L[i] = result
# This can be rewritten using enumerate() as:

for i, item in enumerate(L):
    # ... compute some

def multiply(arr, num):
    for index in range(len(arr)):
        # cal also use enumerate
        arr[index] = arr[index] * num
    return arr
a = [2,4,10,16]
x = multiply(a,5)
print x

>>> S = [x**2 for x in range(10)]
>>> V = [2**i for i in range(13)]
>>> M = [x for x in S if x % 2 == 0]
>>>
>>> print S; print V; print M
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
[0, 4, 16, 36, 64]
#########################

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.items():
     print key, " = ", data

data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']
