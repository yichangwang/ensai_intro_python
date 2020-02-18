# Read doc / Search from Internet
- [Stack Overflow](https://stackoverflow.com/)
- [Python doc](https://doc.python.org) (in [French](https://docs.python.org/fr/3.6/))

# Built-in data structure

## int / float 

## string
- format method

## list / tuple
- methods: `insert`, `append`, `sort`, etc.
- list comprehension
- mutable / immutable object

## dictionary
## set

## boolean type / None type

# Function
- built-in functions (`range`, `print`, `sort`, etc.)
- create / execute a function
- parameter / argument
    - positional argument
    - argument with default value
    - key word argument
- lambda function

# Module
- `__name__ == '__main__'`

# Class
## attribute
- class variable
- instance method
- magic method (`__init__`, `__str__`, `__eq__`, `__add__`, etc.)
## call
```
instance = MyClass()  # there's the __eq__ method in MyClass
another_instance = MyClass()
# call
MyClass.__eq__(instance, another_instance)
instance.__eq__(another_instance)
instance == another_instance  # overload the == operator with __eq__ method
```
# Good to know
- use debugger
- `sys.argv[]`
- closure
- copy, deepcopy
- `id()`, `dir()`, `help()`
- ```
  a = 3
  b = a
  a is b
  ```

- [`venv`](https://docs.python.org/3/tutorial/venv.html) or [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation.html)
