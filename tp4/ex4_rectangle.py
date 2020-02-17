from copy import copy  # shallow copy
from copy import deepcopy
from ex3_point import Point

# un article sur deep copy et shallow copy
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86

class Rectangle:
    
    def __init__(self, x0, y0, x1, y1):
        self.coin_so = Point(x0, y0)  # sud-ouest
        self.coin_ne = Point(x1, y1)  # nord-est

    def __str__(self):
        return "[(" + str(self.coin_so.x()) + ", " + str(self.coin_so.y()) + ") ; (" + \
                str(self.coin_ne.x()) + ", " + str(self.coin_ne.y()) + ")]"


if __name__ == '__main__':
    r1 = Rectangle(1, 2, 3, 4)
    r2 = r1  # pass reference (pass the address in memory)
    r3 = copy(r1)  # make new object for r3.coin_so and r3.coin_ne
    r4 = deepcopy(r1)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nModification du coin_so -> (0,0) de R1.")
    r1.coin_so = Point(0, 0)  # coin_so refers a new Point instance  
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nRéalisation d'une homothétie de 2 sur le coin_ne de R1.")
    r1.coin_ne.homothetie(2)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    r3.coin_ne.homothetie(4)
    print("\nRéalisation d'une homothétie de 4 sur le coin_ne de R3.")
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
