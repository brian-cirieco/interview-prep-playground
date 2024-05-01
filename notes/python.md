# Python

Sources:
- https://www.interviewbit.com/python-interview-questions/

## Types

### Overview
Python is a __strongly typed language__.

_e.g._
```python
>>> "1" + 2
TypeError: can only concatenate str (not "int") to str
```

whereas __dynamically typed languages__ (such as JavaScript) allow for __type-coercion__

_e.g._
```js
>>> "1" + 2
"12"
```
### Type Checking
Type-checking can be done at two stages:
- __static__ - data types are checked _before_ execution
- __dynamic__ - data types are checked _after_ execution

### Lists vs Tuples
__Lists__ and __Tuples__ are both sequence data types. The objects stored in both sequences can have _different_ data types.

Lists:
- use __square brackets__:\
`['sara', 6, 0.19]`
- mutable:\
`my_list[0] = 1` >>> stores 1 at index 0 

Tuples:
- use __parentheses__:\
`('sara', 6, 0.19)`
- immutable:\
`my_tuple[0] = 1` >>> throws an error

### Common Built-In Data Types
Types are not required to be defined explicitly during variable declarations.\
`type()` and `isinstance()` are provided to check types.

Type categories:
- None Type:\
`None` keyword represents null values in Python. Boolean operator can be performed using these NoneType objects.
- Numeric Types:\
There are 3 distinct numeric types - __integers__, __floating-point numbers__, and __complex numbers__. Additionally, __booleans__ are a sub-type of integers.

| Class Name | Description |
| ---------- | ----------- |
|`int`| Stores integer literals including hex, octal, and binary numbers as integers |
| `float` | Stores literals containing decimal values and/or exponent signs as floating-point numbers |
|`complex`| Stores numbers in the form (A + Bj) and has attributes: `real` and `imag`|
|`bool`|Stores boolean value (`True` or `False`)|

## Execution
Python is an __interpreted language__, meaning it executes its statements line by line reading directly from the source code without an intermediate compilation step.\
Others include JavaScript, R, PHP, and Ruby.

## PEP 8
PEP == Python Enhancement Proposal\
Official design document providing information to the Python community.

## Scope
There are 4 scopes in Python (from lowest level to highest level):
1. __local scope__ refers to the local objects available in the current function.
2. __global scope__ refers to the objects available throughout the code execution since their inception.
3. __module-level scope__ refers to the global objects of the current module accessible in the program.
4. __outermost scope__ refers to all the built-in names callable in the program. Objects in this scope are searched last to find the name referenced.

_Note_: Local scope objects can be synced with global scope objects using keywords such as `global`