# https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc

class Test:
    def __init__(self):  # double underscore 
        self.x = 11
        # a convention to declare a private variable (but not so private)
        self._y = 12
        # mangle the attribute names of a class to avoid conflicts of attribute names between classes. 
        self.__z = 13

    def str_(self):
        """single_trailing_underscore_
        => to avoid conflict when having the same name of some exist object
        (variable/function/method/etc.)
        """
        return "I am the str_ method"


a = Test()
print(a.x)
print(a._y)

try:
    print(a.__z)  # AttributeError: 'Test' object has no attribute '__z'
except:
    print(a._Test__z)

print(a.str_())
