import math

class Point:
    """Classe representnat un Point
    """
    def __init__ (self, x, y):
        """ constructs a point from cartesian coordinates x,y"""
        self.__x = float(x)
        self.__y = float(y)
        
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def r(self):
         return math.sqrt(self.__x ** 2 + self.__y ** 2)
    
    def t(self):
        return math.atan2(self.__y, self.__x)
    
    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

    def __eq__(self, autrePoint):
        return isinstance(autrePoint, Point) and \
                          self.x() == autrePoint.x() and \
                          self.y() == autrePoint.y()

    def homothetie(self, k):
        self.__x = self.__x * k
        self.__y = self.__y * k

    def translation(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
    
    def rotation(self, a):
        coord_r = self.r()
        coord_t = self.t() + a
        self.__x = coord_r * math.cos(coord_t)
        self.__y = coord_r * math.sin(coord_t)
