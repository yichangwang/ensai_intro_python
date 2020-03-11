# Concepts from class

## Read doc / Search from Internet

- [Stack Overflow](https://stackoverflow.com/)
- [Python doc](https://doc.python.org) (in [French](https://docs.python.org/fr/3.6/))
- A nice video tutorial on [Python OOP](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

## Built-in data structure

### int / float

### string

- format method

### list / tuple

- methods: `insert`, `append`, `sort`, etc.
- list comprehension
- mutable / immutable object

### dictionary

### set

### boolean type / None type

## Function

- built-in functions (`range`, `print`, `sort`, etc.)
- create / execute a function
- parameter / argument
  - positional argument
  - argument with default value
  - key word argument
- lambda function

## Module

- `__name__ == '__main__'`

## Class

### attribute

- class variable
- instance method

### call

```python
instance = MyClass()  # there's the __eq__ method in MyClass
another_instance = MyClass()
# call
MyClass.__eq__(instance, another_instance)
instance.__eq__(another_instance)
instance == another_instance  # overload the == operator with __eq__ method
```

### inheritance, overload, polymorphism

- magic method (`__init__`, `__str__`, `__eq__`, `__add__`, etc.)


### method (instance), class method, statistic method

## Good to know

- use debugger
- `sys.argv[]`
- closure
- copy, deepcopy
- `id()`, `dir()`, `help()`
- To check the if two objects is the same

  ```python
  a = 3
  b = a
  a is b  # True

  a = {"one": 1, "two": 2, "three": 3}
  b = dict(one=1, two=2, three=3)
  a == b  # True
  a is b  # False
  ```

- [`venv`](https://docs.python.org/3/tutorial/venv.html) or [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation.html)
- use `pylint` (with `graphviz`) to [generate uml graph](./uml_diagrams.rst)