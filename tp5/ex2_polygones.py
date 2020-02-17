import math
class Point():
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def x(self): return self.__x

    def y(self): return self.__y

    def __str__ (self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"


class Polygone():
    def __init__(self, sommets):
        self.sommets = sommets[:]

    def get_sommet(self, i):
        return str(self.sommets[i])

    def aire(self):
        aire = 0.0
        sommets = self.sommets + [ self.sommets[0] ]
        for i in range(len(self.sommets)):
            aire = aire + abs(sommets[i].x() - sommets[i+1].x()) * \
            abs(sommets[i].y() - sommets[i+1].y())
        return 1/2 * aire

    def __str__(self):
        txt = ""
        for i in range(1, len(self.sommets)):
            txt = txt + " ; " + str(self.sommets[i])
        return "[" + str(self.sommets[0]) + txt + "]"


class Triangle(Polygone):
    def __init__(self, a, b, c):
        Polygone.__init__(self, [a, b, c])


class Rectangle(Polygone):
    def __init__(self, xMin, xMax, yMin, yMax):
        Polygone.__init__(self, [Point(xMin, yMin), Point(xMax, yMax)])


class PolygoneRegulier(Polygone):
    def __init__(self, centre, rayon, nbSommets):
        sommets = []

        for i in range(nbSommets):
            xi = centre.x() + rayon * math.cos(2 * math.pi * i / nbSommets)
            yi = centre.y() + rayon * math.sin(2 * math.pi * i / nbSommets)
            sommets.append(Point(xi, yi))
            Polygone.__init__(self, sommets)

if __name__ == '__main__':
    tri = Triangle (Point(0, 0), Point(0, 3), Point(3, 0))
    print("Triangle: ")
    print(tri)
    print(tri.aire())
    rec = Rectangle (1, 2, 3, 4)
    print("\nRectangle: ")
    print(rec)
    print(rec.aire())
    pol = PolygoneRegulier (Point(0, 0), 5, 4)
    print("\nPolygone régulier: ")
    print(pol)
    print(pol.aire())