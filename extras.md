# Extras

## More on Python language and syntax

### Lexicon

1. Two or more physical lines may be joined into logical lines using backslash (\).
2. Expressions in (), \[] or {} can be split over more than one physical line without using \.
3. A ```TabError``` is raised when indentation is inconsistent.
4. In CLI, ```_``` is a variable that stores the most recently computed value.
5. f-strings cannot be used as docstrings, even if they do not include expressions.
6. An _ is ignored for determining the numeric value of the literal and can be used to group digits for enhanced
readability. e.g. 100_000, 0x_24.
7. Use ```j``` for imaginary numbers. e.g. 2.34_244e2j.

The following are examples of string formatting. Courtesy: Python Documentation.

![Examples of string formatting](/images/string_formatting.png "Examples of string formatting")

### Data model

Every object has an identity, a type and a value. An object’s identity never changes once it has been created; think of it as the object’s address in memory.

1. ```is``` operator compares the identity of two objects.
2. ```id(x)``` is the memory address where x is stored.
3. ```type()``` returns an object’s type (which is an object itself). Like its identity, an object’s type is also unchangeable.

An object’s mutability is determined by its type; e.g., numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

1. After c = \[]; d = \[], c and d are guaranteed to refer to two diﬀerent, unique, newly created empty lists.
2. c = d = \[] assigns the same object to both c and d.

The built-in function ```ord()``` converts a code point from its string form to an integer in the range 0 - 10FFFF; ```chr()``` converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object. ```str.encode()``` can be used to convert a str to bytes using the given text encoding, and ```bytes.decode()``` can be used to achieve the opposite.

A function has the following special attributes:

```python
__doc__ # docstring, not inherited by subclasses
__name__ # function's name
__qualname__ # function's qualified name
__module__ # name of the module where the function is defined in
__defaults__ # tuple containing default argument values
__code__ # code object representing the compiled function body
__dict__ # namespace supporting arbitrary function attributes
__closure__ # None or a tuple of cells that contain bindings for the function’s free variables
__kwdefaults__ # dict containing defaults for keyword-only parameters
```




