from copy import copy
from copy import deepcopy
from ex3_point import Point

class Rectangle:

    def __init__ (self, x0, y0, x1, y1):
        self.coinNO = Point(x0, y0)  # north west corner
        self.coinSE = Point(x1, y1)

    def __str__ (self):
        return "[(" + str(self.coinNO.x()) + ", " + str(self.coinNO.y()) + ") ; (" + \
                str(self.coinSE.x()) + ", " + str(self.coinSE.y()) + ")]"


if __name__ == '__main__':
    r1 = Rectangle (1, 2, 3, 4)
    r2 = r1
    r3 = copy(r1)
    r4 = deepcopy(r1)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nModification du coinNO -> (0,0) de R1.")
    r1.coinNO = Point(0, 0)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nRéalisation d'une homothétie sur le coinSE de R1.")
    r1.coinSE.homothetie(2)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    r1 = Rectangle (1, 2, 3, 4)
    r2 = r1
    r3 = copy(r1)
    r4 = deepcopy(r1)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nModification du coinNO -> (0,0) de R1.")
    r1.coinNO = Point(0, 0)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))
    print("\nRéalisation d'une homothétie sur le coinSE de R1.")
    r1.coinSE.homothetie(2)
    print("r1: " + str(r1) + " ; r2: " + str(r2) + " ; r3: " + str(r3) + " ; r4: " + str(r4))