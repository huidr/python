# Intermediate

## More on functions

### Closure

Nested functions can access variables of the enclosing scope. The criteria for a closure are:

1. Have a nested function.
2. The nested function references a variable defined in the enclosing function.
3. The enclosing function returns the nested function.

```python
def general_multiplier(n):
  def multiplier(x):
    return x*n
  return multiplier

times_2 = general_multiplier(2)
times_3 = general_multiplier(3)

times_2(10) # 20
times_3(10) # 30

del general_multiplier

# still works after the function has been removed
times_2(8) # 16
times_3(8) # 24
```

The value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

When to use closure?

1. If there are few methods of a class, it might be a better idea to use a closure instead of that class.
2. To avoid the use of global variables and provide some form of data hiding.

```python
class A:
  def __init__(self):
    self.data = []
  
  # make its instances callable
  def __call__(self, a):
    self.data.append(a)
    _sum = sum(self.data)
    return _sum
  
a = A()

# call the instance
a(1) # 1
a(2) # 3
a(3) # 6
a(4) # 10

# implement the same class as closure
def f():
  data = [] # act like attributes
  
  def sum(a):
    data.append(a)
    _sum = sum(data)
    return _sum
  return sum

t = f()
t(1) # 1
t(2) # 3
t(3) # 6
t(4) # 10
```

When to not use closure?

1. When the number of attributes and methods grow larger, use a class and not a closure.

```python
# x, y, z are nonlocal variables of g
def f():
  x = 2
  y = 4
  z = 6
  def g(a, b, c):
    return x*a, y*b, z*c
  return g

s = f()

# check if s is a closure function
s.__closure__ # returns a tuple of cell objects

# the cell object has the attribute cell_contents which stores the closed value
# this will return the values of the nonlocal varibles which are 2, 4, 6
s.__closure__[0].cell_contents # 2
s.__closure__[1].cell_contents # 4
s.__closure__[2].cell_contents # 6
```

Use the ```nonlocal``` keyword to modify a variable in the outer function scope.

```python
def outer():
  x = 8
  def inner():
    nonlocal x # x must already be defined in the outer scope
    x = 2
  print("x =", x)
  inner()
  print("x =", x)

outer()
# prints
# x = 8
# x = 2
```

### Higher-order functions

Almost everything in Python is an object, i.e., it is an subclass or an instance of a subclass of the ```Object``` class. Hence, functions are also objects and they can be passed as arguments to other functions or returned from other functions.

```python
def f(text):
  return text.upper()
  
def g(text):
  return text.lower()

# function as a parameter
def h(func, text):
  s = func(text)
  print(s)
  
# function as arguments
h(f, 'Python') # PYTHON
h(g, 'JavaScript') # javascript
```

The following are also possible.

1. Assign the function to a variable.
2. Use ```del``` to delete functions.
3. Functions can be stored in lists, etc.

```python
def f(n):
  i = 2
  a = []
  def g(x):
    return x*i
  while (i<=n):
  
    # store functins in a list
    a.append(g)
    i += 1
    
  # return a list of functions
  return a

# assign the function to a variable
h = f

# h and f are two references to the function
# let's delete f and work with h
del f

# unpack the functions
x, y, z = h(4)

# all are multipliers of 5
x(5) # 25
y(7) # 35
z(9) # 45
```

### Decorators

Decorators are the most common use of higher-order functions. They take in functions (as arguments), add functionality (decorate) and return it.

```python
def decorate(f):
  def inner():
    print("Just got decorated.")
    f()
  return inner

def g():
  print("I am just a function")

# send g to decorate()
# h is also a closure function
h = decorate(g)

g()
# I am just a function

h()
# Just got decorated
# I am just a function
```

In the above, one could have written:

```python
g = decorate(g)
```

The function g just got upgraded (or decorated). This is exactly what a decorator is. Python has a special syntax for this.

```python
@decorate
def g():
  print('I am just a function')

# above code is equivalent to the following
def g():
  print('I am just a function')
g = decorate(g)
```

Parametrized functions can be decorated like the following:

```python
def smart_divider(f):
  def inner(a, b):
    if b == 0:
      print("Can't divide by zero.")
      return
    return f(a, b)
    
  return inner
  
@smart_divider
def divider(x, y):
  return x/y
  
divider(4, 2) # 2.0

divider(4, 0)
# Can't divide by zero.
```

Parameters of the nested inner() function inside the decorator is the same as the parameters of functions it decorates. A general decorator can be made using ```*args``` (which accepts tuple of positional arguments) and ```**kwargs``` (which accepts dictionary of keyword arguments).

```python
def decorate(f):
  def inner(*args, **kwargs):
    print('I can decorate any function')
    return f(*args, **kwargs)
    
  return inner
```

Decorators can also be chained. One can decorate functions with same or different decorators many times.

```python
def first_decorator(f):
  def inner(*args, **kwargs):
    print('I am first decorator')
    return f(*args, **kwargs)
    
  return inner
  
def second_decorator(f):
  def inner(*args, **kwargs):
    print('I am second decorator')
    return f(*args, **kwargs)
    
  return inner

@second_decorator
@first_decorator
def adder(*args):
  return sum(args)

adder(1, 2, 3)
# I am second decorator
# I am first decorator
# 6

# an equivalent way of decorating
adder = second_decorator(first_decorator(adder))
```

One can pass arguments to the decorator itself. To achieve this, define a decorator maker that accepts arguments then define a decorator inside it. Henceforth, we replace inner() by wrapper() because it wraps around the orginal function, decorating it.

```python
def decorator_maker(dec_arg_1, dec_arg_2):
  def decorator(func):
    def wrapper(*args, **kwargs):
      ''' I am wrapper '''
    
      print('I am the wrapper function')
      print(dec_arg1, dec_arg_2)
      return func(*args, **kwargs)
    
    return wrapper
  return decorator

@decorator_maker(4, 8)
def f():
  ''' I am f '''
  return 'I want to get decorated'

f()
# I am the wrapper function
# 4 8
# 'I want to get decorated'
```

In trying to get metadata of the undecorated function, you get the metadata of the wrapper() function instead which might be frustrating during debugging process. Python offers ```functools.wraps``` decorator which copies the lost metadata from the undecorated function to the decorated closure.

```python
# try to get metadata of f
f.__name__ # 'wrapper'
f.__doc__ # ' I am wrapper '

# the metadata of f() is hidden or overriden by wrapper()

import functools

def decorator(func):
  @functools.wraps(func)
  def wrapper():
    ''' I am wrapper '''
    
    return func().upper()
  return wrapper

@decorator
def printer():
  ''' I am printer '''
  
  return 'Python'
  
# check metadata
printer.__name__ # printer
printer.__doc__ # I am printer
```

### ```@property``` decorator

Python offers ```property()``` which is used to create property of a class. It has the following syntax.

```python
property(getter=None, setter=None, deleter=None, doc=None)

# getter() – used to get the value of attribute
# setter() – used to set the value of attribute
# deleter() – used to delete the attribute value
# doc() – string that contains the documentation (docstring) for the attribute
```

If doc isn’t provided, property() takes the docstring of getter().

```python
class Person:
  def __init__(self, val = 0):
    self.age = val
  
  # getter
  def getter(self):
    return self._age
    
  # setter
  def setter(self, val):
    if val < 0:
      raise ValueError('Age cannot be negative.')
    
    # note the use of private variable
    self._age = val
  
  # give age a property from getter, setter
  age = property(getter, setter)

p = Person(-4) # ValueError: Age cannot be negative
p = Person(24) # okay
p.age = -12 # ValueError: Age cannot be negative

# comment the line where we used property(), then try the following
p.age = -12 # okay
p.__dict__ # {'age': -12}

# uncomment the line where we used property(), then try the following
p.age = 26
p.__dict__ # {'_age': 26}

# interesting, when we modified age, it reflects on _age and __dict__ shows only _age as attribute
```

In short, the attribute age has gained some properties from getter, setter functions. Any code that retrieves the value of *age* automatically calls getter() instead of a dictionary (```__dict__```) look-up. Any code that assigns a value to *age* automatically calls setter().

Also, the actual age value is stored in the private *_age* variable. The age attribute is just a property object which provides an interface to this private variable.

Python offers ```@property``` decorator as a syntactic sugar for ```property()```.

```python
class Person:
  def __init__(self, val = 0):
    self.age = val
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, val):
    if val < 0:
      raise ValueError('Negative value is illegal')
    self._age = val
```

This code has the same functionality as the one we wrote using property().

### RegEx

Python has ```re``` module to work with regular expressions. See [regex101](https://regex101.com/) for building, testing, debugging regular expressions.

```python
# match a RegEx against a string
# returns a re.Match object if matching is found, else returns None
re.match('^a.[s].k*t$', 'apsyt') # match = 'apsyt'
re.match('\bfoot[pqr]', 'footr') # None
re.match('a+j?s{1,2}', 'aaajssh') # match = 'aaajss'
re.match('^p.*{tyz}h?(k|o)n', 'python') # None
re.match('^p.*t+hon$', 'python')

# find all matches and return a list
re.findall('\d+', 'I am 18, weighs 64 kgs and 6 ft tall.') # ['18', '64', '6']
re.findall('\bse', 'Twenty seconds ago, I set the timer.') # []
re.findall('[bc].r', 'I took the car to the bar') # ['car', 'bar']
re.findall('a{1,2}', 'It was my cat') # ['a', 'a']
re.findall('a*j', 'I love jazz') # ['j']

# split the string where there is a match and return a list of strings where the splits have occurred.
re.split('\d+', 'I am 18, weighs 64 kgs and 6 ft tall.') # ['I am ', ', weights ', ' kgs and ', ' ft tall.']
re.split('\bse', 'Twenty seconds ago, I set the timer.') # ['Twenty seconds ago, I set the timer.']
re.split('[bc].r', 'I took the car to the bar') # ['I took the ', ' to the ', '']
re.split('a{1,2}', 'It was my cat') # ['It w', 's my c', 't']
re.split('a*j', 'I love jazz') # ['I love ', 'azz']

# some other methods

# return a string where matched occurrences are replaced with the content of replace variable
re.sub(pattern, replace, string)

# look for the first location where the RegEx pattern produces a match with the string
re.search(pattern, str)
```

See ```re``` library for more functionality.

### Concurrent programming

A process can broken down into threads and each thread can be run by different cores (of a multi-processor) simultaneously, thus reducing the time spent in solving the problem. This is called threading. In Python, Global Interpreter Lock (```GIL```) allows only one thread to hold the control of the Python interpreter. This means you can execute only one thread at a given time. Thus, there is no true threading in Python.

Despite there is no true threading in Python, there is ```threading``` library which allows you to use threads. Let's explore this.

```python
import threading
import time

def f():
  for i in range(10000000):
    pass

def g():
  # start time
  t = time.time()
  f()
  f()
  # stop time
  s = time.time()
  
  # return execution time
  return s - t
  
# use threading
def h():
  t = time.time()
  
  # create two threads
  thread_1 = threading.Thread(target = f)
  thread_2 = threading.Thread(target = f)
  
  # start threads
  thread_1.start()
  thread_2.start()
  
  # ensure that threads have been terminated
  thread_1.join()
  thread_2.join()
  
  s = time.time()
  
  # return execution time
  return s - t

# without threading
g()

# with threading
h()
```

Funnily enough, threading might actually consume more execution time than without threading. In fact, in many cases it actually slows down execution rather than speed it up. However if the code includes I/O operations, file operations or user interaction, threading can actually be very beneficial.

### Parallel programming

Instead of ```threading```, one can use ```multiprocessing``` to break the program into processes rather than threads. Since processes are not constrained by GIL, multiple cores can be used for multiple processes at a given time. The syntax is very similar.

```python
import multiprocessing
import time

def f():
  for i in range(10000000):
    pass
    
def g():
  t = time.time()
  
  # execute f four times
  for i in range(4):
    f()
    
  s = time.time()
  return s - t
  
def h():
  t = time.time()
  
  # create four processes
  proc_1 = multiprocessing.Process(target = f)
  proc_2 = multiprocessing.Process(target = f)
  proc_3 = multiprocessing.Process(target = f)
  proc_4 = multiprocessing.Process(target = f)

  # start processes
  proc_1.start()
  proc_2.start()
  proc_3.start()
  proc_4.start()
  
  # block the execution of the processes until they terminate 
  proc_1.join()
  proc_2.join()
  proc_3.join()
  proc_4.join()

  s = time.time()
  return s - t

# without multiprocessing
g()

# with multiprocessing
h()
```

In the above case, multiprocessing significantly speeds up execution time. In general, use multiprocessing on computationally intensive code and threading on code which relies on I/O, file operations and user interactions.

Each process is independent and has its own memory space.

```python
import os
import multiprocessing

lst = []

def f(nums):
  global lst
  for i in nums:
    lst.append(i)
  print('lst =', lst)
  
  # os.getpid() returns the process ID of the process running this code
  print(os.getpid())

nums = [2, 4, 6, 8]
proc_1 = multiprocessing.Process(target = f, args = (nums, ))
proc_1.start()

# lst = [2, 4, 6, 8]
# 4859 (this is PID, might be different on another run)

print(lst) # []
os.getpid() # 4842

# lst in main process is not affected by what happens in process 1
```

Sometimes you may need the processes to communicate or have shared memory. For this, ```multiprocessing``` provides ```Array``` and ```Value``` objects.

```python
import os, multiprocessing

def f(lst, val):
  for i, v in enumerate([2, 4, 6, 8]):
    
    # cannot use append method (why?)
    lst[i] = v
  
  # you need [:] operator to convert it into normal list form
  # you need value method of Value class to access or assign values
  val.value = sum(lst[:])
  print ('lst = ', lst[:])
  print ('sum = ', val.value)
  
# lst should hold 4 'i'nteger values 
lst = multiprocessing.Array('i', 4)

# val should hold integer value
val = multiprocessing.Value('i')

# you can give initial value as
val = multiprocessing.Value('i', 0)

# you should give the Array and Value objects as arguments
proc_1 = multiprocessing.Process(target = f, args = (lst, val))

proc_1.start()
# lst = [2, 4, 6, 8]
# sum = 20

# changes are reflected in the main process
print(lst[:]) # [2, 4, 6, 8]
print(val.value) # 20
```




### Metaprogramming







