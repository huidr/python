
# Fundamentals

### Variables

```python
# multiple assignment
a, b = 0, 1 
```
  
In multiple assignment, the expressions on the right-hand side are all evaluated ﬁrst before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

### Arithmetic

In interactive mode, the last printed expression is assigned to the variable _

```python
a + b; 
a - b;
a * b;
a / b; # returns a float
a // b; # floor division
a % b;
a ** b; # a to the power b
```
  
## Strings

```python
# raw string
print(r'\usr\bin\name') # characters prefaced by \ will NOT be interpreted as special characters
 ```
  
Operations on strings, lists, etc.
  
```python
# concatenation
name = 'Computer' + 'programming'
name = 'Computer' 'programming' # useful for long strings, works only for string literals
  
# slicing [start:stop:step]
subname = name[2:8] # step = 1 (by default)
subname = name[-1] # the last entry
subname = name[-1::-1] # reverse string
```
  
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are
automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.
 
### Basics

```python
sys.argv // a list that stores script name and additional arguments
sys.argv[0] // script name
sys.argv[1] // first argument, if it exists
```
  
## Control Flow
 
```if```, ```elif```, ```else``` &mdash; elif and else are optional, elif can be one or more.
 
```python
if (condition):
  do_this
elif (condition):
  do_this
else:
  do_this
```

```for``` &mdash; iterates over an iterable (like list, string, dictionary, etc). Code that modiﬁes a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection.

```python
# iterate over a copy
for user, status in users.copy().items():
  if status == 'inactive':
    del users[user]
      
# create a new collection
active_users = {}
for user, status in users.items():
  if status == 'active':
    active_users[user] = status
```
  
```range()``` &mdash; accepts arguments as (start:stop:step), generates arithmetic progressions.

```python
# handy in looping, default values: start = 0, step = 1
for i in range(10):
  do_this
    
# turn it into a list
nums = list(range(40, 20, -2))
  
# sum it up because it is an iterable
sum(range(10))
```

```break```, ```continue```, else-in-loop (for-else, while-else)

```python
for i in range(10):
  for j in range(5):
    if (condition):
      break # terminate the innermost loop containing this statement
    if (condition):
      continue # skip to the next iteration of the innermost loop containing this statement
  else:      
    do_this # execute this if the loop was not terminated by break
```

```pass``` &mdash; handy when statement is required syntactically but the program requires no action.

```python
# commonly used for creating minimal classes
class EmptyClass:
  pass
  
# also used as a place-holder
def func(*args):
  pass
```

## Functions

```python
def myfunction(*args):
  ''' docstring ''' # can be fetched by myfunction.__doc__
  do_this
```
    
1. Global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.
2. Functions always return a value. It returns ```None``` if there is no ```return``` statement.

### Default arguments

```python
def myfunction(name, type='language', id=0):
  do_this
  
# different ways to call the above function
myfunction('Python')
myfunction('van Rossum', 'programmer')
myfunction('Aventador', 'car', 10)
```

The default value is evaluated only once even when the function is called multiple times. This makes a diﬀerence when the default is a mutable object such as a list, dictionary, etc. See the following.

```python
def f(a, L=[]):
  L.append(a)
  return L
  
print(f(1)) # [1]
print(f(2)) # [1, 2]
print(f(3)) # [1, 2, 3]
```

### ```*args``` and ```**kwargs```

Keyword arguments must follow positional arguments (if any) in function call arguments list.

```python
# the above function can be called as
myfunction(type='programmer', id=24, name='Knuth')
myfunction('van Rossum', id=10, type='programmer')
```
  
A parameter of the form ```*args``` receives a tuple while ```**kwargs``` receives a dictionary. Note that if both exist, ```**kwargs``` should follow ```*args```. Also, keywords become the keys of the dictionary.

```python
def insert_data(name, *marks, **grades):
  print(name)
  print(marks)
  print(grades)
    
insert_data('John',
        83, 77, 80,
 	algorithms='A', topology='B', electrodynamics='A')
  
# this becomes
# name = 'John'
# marks = (83, 77, 80)
# grades = {'algorithms':'A', 'topology':'B', 'electrodynamics':'A'}
```

### Parameter list

One can specify only positional arguments, standard (either positional or keyword) and only keyword argumements in the parameter list. The general form of the parameter list look something like this:

```
def f(pos_only, /, pos_or_kw, *, kw_only)
```
  
pos_only arguments cannot receive keyword arguments and so on. If there is no ```/``` and ```*```, the arguments are standard (either positional or keyword).

```python
def get_info(name, /, age, *, weight):
  print(name, age, height, sep=' ')
  
# possible function calls
get_info('Tom', 24, weight=76)
get_info('Tom', age=24, weight=76)

# some ways to write parameters list
def get_info(name, /) # receive pos_only arguments
def get_info(*, weight) # receive kw_only arguments
```

Dictionaries can deliver keyword arguments with the ```**```-operator.

```python
def f(name, weight=50, beverage='beer'):
  print(f'{name} weighs {weight} kilos and drinks {beverage}.')
  
d = {'name':'Robert', 'weight':58, 'beverage':'vodka'}
  
# then call the function this way
f(**d)
```

### Lambdas

Lambda functions can take any number of arguments but can only have one expression.

```python
f = lambda x, y : x ** y
  
print(f(2,4)) # 2 to the power 4
```

Lambdas are better used inside function definitions when an anonymous function is required for a short period of time.

## Data Structures

### Lists

The following are some common list methods.

```python
list.append(x)
list.extend(iterable)
list.insert(index, x)
list.remove(x) # removes first occurrence of x, returns ValueError if not found
list.pop([index]) # returns the popped off item
list.clear()
list.index(x [, start[, stop]]) # finds the index of x searching in list[start:stop]
list.count(x)
list.sort(*, key=None, reverse=False)
list.reverse()
list.copy() # returns a copy of the list
```

Lists can be used as **stacks** &mdash; use ```list.append()``` and ```list.pop()``` to add/remove items at the top of the stack. Although lists can be used as **queues** as well, it is not recommended as performing inserts/pops from the beginning of a list is slow (as it involves shifting of all other elements by one) &mdash for this purpose, use ```collections.deque``` which was designed to have fast appends/pops from both ends.

```python
from collections import deque
queue = deque(['Newton', 'Maxwell', 'Einstein'])
queue.append('Dirac')
queue.popleft()
  
# can be used as stack as well
queue.pop()
```

List comprehensions provide a concise way to create lists and other data structures.

```python
pairs = [(x, y) for x in [2, 3, 7] for y in [1, 3, 4] if x != y]
# [(2, 1), (2, 3), (2, 4), (3, 1), (3, 4), (7, 1), (7, 3), (7, 4)]
  
a = ['  time', 'money  ', ' skill ']
b = [x.strip() for x in old_names]
# b = ['time', 'money', 'skill']
  
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for elem in vec item in elem]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
  
List comprehensions can be nested.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
```
  
```del``` can be used to remove items from a list given its index instead of its value.

```python
a = ['Tom', 'Huck', 'Mark']
del a[2]
del a[1:] # use slicing
del a # delete entire variables
```
  
### Tuples

Tuples are like lists but immutatable.

```python
# tuple packing
t = 2, 4, 6
  
# sequence unpacking
a, b, c = t
  
# nesting
u = t, ('Python', 'C++')
  
# can contain mutable objects
s = ([1, 2], [3, 4])
  
# empty tuple
s = ()
  
# one-element tuple
s = 1,
```

### Sets

Sets are unordered collections and have no duplicate elements. One can perform set operations like union, intersection, etc.

```python
# initialization
vowels = set('aeiou')
letters = {'a', 'b', 'c', 'l', 'm'}
  
# membership testing
if 'e' in vowels:
  print("Yes")
 
# set union
u = vowels | letters
  
# set intersection
u = vowels & letters
  
# set difference
u = vowels - letters
  
# symmetric difference
u = vowels ^ letters
  
# set comprehensions
a = {x for x in 'python' if x not in 'javascript'}
```

Sets can be iterated over. Common uses for sets are fast membership testing, removing duplicates from a sequence, and computing
mathematical operations such as intersection, union, diﬀerence, and symmetric diﬀerence.

Frozen sets represent an immutable sets and are created by the built-in ```frozenset()``` constructor.

### Dictionaries

A dictionary is just a set of *key: value* pairs where *value* can be almost any Python object while *key* must be immutable (strings, numbers or tuples that do not contain mutable objects directly or indirectly).

```python
# empty dictionary
d = {}
  
# add elements
d['jack'] = 24
  
# delete elements
del d['jack']
  
# get a list of its keys
keys = list(d)
  
# get a sorted list of its keys
keys = sorted(d)
  
# membership test
'jack' in d
'jack' not in d
  
# dict comprehensions
d = {x: x**2 for x in range(10)}
  
# dict() constructor
d = dict([(1, 1), (2, 4), (3, 9)])
  
# if keys are simple strings
d = dict(jack = 24, jill = 36)
```
  
Dictionaries preserve insertion order. Replacing an existing key does not change the order, however removing a key and re-inserting it will add it to the end instead of keeping its old place.
  
### Looping techniques

When looping through dictionaries, use ```items()``` to retrieve key, value pairs.

```python
d = dict(one = 1, two = 2, three = 3)
for key, value in d.items():
  print(key, value)
```
  
When looping through sequences, use ```enumerate()``` to retrieve index, value pairs.

```python
lst = ['time', 'money', 'skill']
for index, value in enumerate(lst):
  print(index, value)
```
 
When looping over two or more sequences simultaneously, use ```zip()``` to pair the entries. If the sequences are of different length, it loops until the smallest sequence is looped over.

```python
sqs = [1, 4, 9, 16, 25]
cbs = [1, 8, 27, 64, 125]
for s, c in zip(sqs, cbs):
  print(s, c)
```

To loop over a sequence in reverse, ﬁrst specify the sequence in a forward direction and then call ```reversed()```.

```python
for i in reversed(range(10)):
  print(i)
```
  
To loop over a sequence in sorted order, use the ```sorted()``` function which returns a new sorted list while leaving the source unaltered.

```python
seq = [x in x in range(10, 0, -1)]
for i in sorted(seq):
  print(i)
```
  
To loop over unique elements of a sequence in sorted order, you ```sorted(set(sequence))```.

### Comparisons

Comparisons between sequences of the same type are lexicographical. Also, comparisons can be chained.

```python
[1, 2, 3] < [1, 2, 4]
'C' < 'Java' < 'Python'
(1, 2, 3, 4) < (1, 3)
(1, 1) < (1, 2) == (1.00, 2.00)
```

The conditions used in ```while``` and ```if``` statements can contain any operators, not just comparisons.

## Modules

### Importing

The following are different ways of importing modules.

```python
import sys
from math import e, pi
from os import *
import matplotlib.pyplot as plt
from numpy import array as arr
```

Defined in ```sys``` module, the variable ```sys.path``` is a list of strings that determines the interpreter’s search path for modules. It can modified as follows:

```python
sys.path.append('/home/user/python/modules')
```

Use ```dir()``` to find out all names which a module defines. Without arguments, it displaces the names you have defined currently.

```python
dir(sys)
  
# find out built-in functions and variables
dir(builtins) 
```

### ```main()``` function

To add versatility to a python file, one can add the ```main()``` function so that it can be used both as a script or a module.

```python
def main():
  do_this
  
if __name__="__main__":
  main()
```

### Packages

A package is a collection of modules. The modules may be put in hierarchical directory system. To make the interpreter treat a directory of modules as if it were a package in itself, put ```__init__.py``` in the directory even if it is an empty file.

When using ```from package import item```, the item can be either a submodule (or subpackage) of the package or some other name defined in the package. Contrary to this, when using ```import item.subitem.subsubitem```, each item except the last must be a package and the last item must be a module or package but can't be a class or function or variable defined in the previous item.

Suppose a ```__init__.py``` file of a directory (package) contain the following code.

```python
__all__ = ["effects", "saver", "bottle"]
```

The following code only imports the modules defined in ```__all__``` even if there are other modules in the package. In fact, avoid using ```from package import *``` syntax to avoid clashes and confusion.

```python
from package import *
```

One can write relative imports using leading dots to indicate the current and parent packages involved.

```python
from . import saver
from .. import hubs
from ..lines import senses
```

## I/O

### Formatting

```f```-strings and ```str.format()``` are used when strings contain variables and expressions.

```python
name = 'Robert'
  
string = f'I call him {name}'
string = 'I call him {}'.format(name)
  
string = '{} is {}.'.format('Tom', 'insame')
  
# using keyword arguments
string = '{name} is nice.'.format(name = 'Tom')
  
# using integer markers
string = '{0} is {1}. {0} is good.'.format('Life', 'enjoyable')
  
# using both intgers markers and keyword arguments
string = 'I like {0}, {1} and {var}.'.format('Python', 'Java', var = 'C++') 
  
# using dictionaries
d = dict(Tom = 6, Sam = 4, John = 2)
s = '{John:d}, {Tom:d}, {Sam:d}'.format(**d) 
# s = '6, 4, 2'
  
# print table of squares and cubes with columns aligned
for x in range(10):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```
  
One can format the number of digits after the decimal point.

```python
from math import pi
text = f'The value of pi is approximately {pi:.4f}.'
# automatically rounds upto 4 decimal points
```
  
Passing an integer after the ':' will cause that ﬁeld to be a minimum number of characters wide. This is useful for making columns line up.

```python
d = dict(February = 28, March = 31, April = 30)
for k, v in d.items():
  print(f'{k:10} has {v:2d} days')
```
  
```str.zfill()``` pads a numeric string on the left with zeroes.

```python
'71'.zfill(5) # 00071
```
  
### Reading/writing files

A good way of doing this is by using ```with``` keyword.

```python
with open('file.txt', 'r+') as f:
  pass
```

Assuming a file object f has been created, the following are some of functionalities available.

```python
# read the entire file
f.read()
  
# read size characters (in text mode) or size bytes (in binary mode)
f.read(size)
  
# read a single line
f.readline()
  
# for reading lines, loop over the file object
for line in f:
  print(line, end = ' ')
  
# read all lines in a list, use any of the following
list(f)
f.readlines()
  
# write a string to a file, returns the number of characters written
f.write('This is me\n')
  
# return an integer giving the file object's current position
f.tell()
  
# change the file object's position
# whence is the reference point, defaults to 0
f.seek(offset, whence)
```
  
### Using JSON

The standard module called ```json``` can take Python data hierarchies, and convert them to string representations; this process is called **serializing**.
Reconstructing the data from the string representation is called **deserializing**.

```python
import json
  
# serialize
json.dumps(obj)
  
# deserialize
json.loads(s)
  
# serialize to a text file
# assume f is the file object
json.dump(obj, f)
  
# decode the object again
x = json.load(f)
```

## Exceptions

### Handling exceptions

The general syntax is

```python
try:
  # code_to_try
  if (condition):
    raise ExceptionOne
except ExceptionOne:
  # do_this
except (ExceptionTwo, ExceptionThree):
  # do_this
else:
  # do_this_if_no_exception_occurred
finally:
  # do_this_always
```

The use of the ```else``` clause is better than adding additional code to the ```try``` clause. The ```Exception``` class is the base class for all exceptions (including built-in). Hence writing ```except Exception``` is the same as writing only ```except```.

The except clause may specify a variable after the exception name. One may also instantiate an exception ﬁrst before raising it and add any attributes to it as desired.

```python
try:
  raise Exception('discord', 'me')
except Exception as obj:
    
  type(obj)
  # <class 'Exception'>
    
  obj.args
  # ('discord', 'me')
    
  obj
  # ('discord', 'me')
    
  s, t = obj.args
  # s = 'discord', t = 'me'
```
  
### Raising exceptions

The ```raise``` statement forces a specified exception to occur. Its sole argument must be either an exception instance or an exception class (derived from ```Exception```). A standalone ```raise``` with no arguments re-raises the exception (this is cool when you need to see if an exception has occurred).

```python
try:
  raise ValueError('message')
except ValueError:
  print('There was an exception')
    
  # re-raise ValueError
  raise
```
  
Exceptions can also be chained using ```raise SomeException from exc```, where exc must be exception instance or None. This can be useful in transforming exceptions.

```python
def f():
  raise ValueError
  
try:
  f()
except ValueError as exc:
  raise RuntimeError('message') from exc
```

### User-defined exceptions

It is a common practice to create a base class for exceptions deﬁned by a module, and subclass that to create speciﬁc exception classes for different error conditions.
    
```python
class Error(Exception):
  ''' Base class for exceptions in this module. '''
  pass
    
class InputError(Error):
  ''' Exceptions raised for errors in the input. 
    
  Atrributes:
    expression --- input expression in which the error occurred
    message --- explanation of the error
  '''
    
  def __init__(self, expr, msg):
    self.expression = expr
    self.message = msg
    
class TransitionError(Error):
  ''' Raised when an operation attempts a state transition that's not allowed.
    
  Attributes:
    previous --- state at beginning of transition
    next --- attempted new state
    message --- explanation of why the specific transition is not allowed
  '''
    
  def __init__(self, prev, nxt, msg):
    self.previous = prev
    self.next = nxt
    self.message = msg
```

### Clean-up actions

The ```finally``` clause is executed in any event.

- If the exception is not handled by an ```except``` clause, the exception is re-raised after the ```finally``` clause has been executed.
- An exception could occur during execution of an ```except``` or ```else``` clause. Again, the exception is re-raised after the ```finally``` clause has been executed.
- If the ```finally``` clause executes a *break*, *continue* or *return* statement, exceptions are not re-raised.
- If the ```try``` statement reaches a *break*, *continue* or *return* statement, the ```finally``` clause will execute just
prior to the *break*, *continue* or *return* statement’s execution.
- If a ```finally``` clause includes a *return* statement, the returned value will be the one from the ```finally``` clause’s *return* statement, not the value from the ```try``` clause’s *return* statement.

In real world applications, the ```finally``` clause is useful for releasing external resources (such as ﬁles or network connections), regardless of whether the use of the resource was successful.

## Classes

### Objects

The syntax of class definition looks like:

```python
class ClassName:
  ''' docstring '''
    
  # constructor
  def __init__(self, *args):
    pass
      
  # shared by all instances
  a = 10
  def f(self, *args):
    pass
```

Objects are instances of its class. Suppose A is a class whose constructor takes only one positional argument ```self```. Also suppose f is a method defined in A taking only ```self``` argument.

```python
# instantiate an object
a = A()
  
# the following are equivalent
A.f(A)
A.f(a)
a.f()

# define new attributes of a
a.x = 4
  
# define new attributes of A
A.y = 6
  
# access newly created attributes
print(a.y)
c = A()
print(c.y)
  
# define new methods of A
def myfunc(self):
  print('Takes 1 positional argument')
def yrfunc():
  print('Takes no positional argument')
A.g = myfunc
A.h = yrfunc
  
# the following are equivalent
A.g(A)
A.g(a)
a.g()
  
# h takes no argument, so it cannot be called by a
A.h() # okay
a.h() # error
  
# define new methods of c
c.p = myfunc
c.q = yrfunc
  
# call the newly created methods of c
c.p() # error, needs 1 argument
c.p(c) # works
c.p(4) # works, the value of the argument does not matter
c.q() # works
c.q(c) # error, takes 0 argument
```

Keep in mind that
- If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance.
- Methods can be defined outside the class (examples shown above).
- Methods may call other methods by using method attributes of the ```self``` argument.

To build something close to *struct* of C/C++, use an empty class.

```python
class Date:
  pass

date = Date()

date.day = 19
date.month = 'December'
date.year = 2021
```

A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary, e.g., C.x is translated to C.```__dict__```\["x"].

The following are some special attributes of a class:

```python
__name__ # class name
__module__ # module name in which the class is defined
__dict__ # dictionary containing the class's namespace
__bases__ # tuple containing the base classes
__doc__ # docstring
```

Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary.

For an object, ```__dict__``` is the attribute dictionary; ```__class__``` is the instance’s class.



### Inheritance

The syntax for derived class definition looks like:

```python
class DerivedClass(BaseClass):
  # regular_class_definition

# base class may be from another module
class DerivedClass(modname.BaseClass):
```

Python has two built-in functions that work with inheritance: ```isinstance(obj, A)``` checks if obj.__class__ is A or some class derived from A, ```issubclass(B, A)``` checks if B is a subclass of A.

```python
class A:
  x = 2
  def f(self):
    print('I am in A.')
  def g(self):
    print('A has me.')

class B(A):
  y = 4
  def p(self):
    print('I am in B.')
  def g(self):
    print('I am also in B.')
  
b = B()

# access A's attributes and methods
print(b.x)
b.f()

# override rule: use the most recent definition (in this case, B's)
b.g()
```

Do multiple inheritance as follows:

```python
class D(A, B, C):
  # class definition
```

If an attribute is not found in D, it is searched for in A, then (recursively) in the base classes of A, and if it was not found there, it was searched for in B, and so on.

### Iterators

One can for-loop over an iterable using ```for i in iterable:```. The following happens behind the scenes.

```python
t = 1, 3, 5, 7
i = iter(t)

next(i) # 1
next(i) # 3
next(i) # 5
next(i) # 7
next(i) # raises error: StopIteration
```

To create a iterable object, one needs to implement ```__iter__()``` and ```__next()__``` and then one can for-loop over this object.

```python
class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)
  
  def __iter__(self):
    return self
   
  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index -= 1
    return self.data[self.index]
 
r = Reverse('python')
for c in r:
  print(c)
```

### Generators

Generators are just like regular functions but use ```yield``` instead of ```return```. Each time ```next()``` is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

```python
def reverse(data):
  for i in range(len(data)-1, -1, -1):
    yield data[i]

for c in reverse('python'):
  print(c, end='')

# prints nohtyp
```

What makes generators so compact is that the ```__iter__()``` and ```__next__()``` methods are created automatically. Generators make it so easy to create iterators with no more effort than writing a regular function.

Generator expressions makes building generators easy by creating anonymous generator functions. The syntax for generator expression is just like that of a list comprehension with parentheses instead. A list comprehension produces an entire list while the generator expression produces one item at a time.

```python
# sum of squares
sum(i*i for i in range(10)) 

# inner product
xv = [2, 4, -1]
yv = [1, -1, -8]
sum(x*y for x,y in zip(xv, yv))

unique_words = set(word for line in page for word in line.split())
```

### Coroutine functions

