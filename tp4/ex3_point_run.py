from ex3_point import Point

class LignePol:
    def __init__ (self, sommets):
        """Construit une ligne polygonale à partir d'une 'list' de 'Point'"""
        self.__sommets = sommets

    def getSommet (self, i):
        """Retourne le sommet numéro i"""
        return self.__sommets[i-1]

    def setSommet (self, i, p):
        """Rajoute le sommet numéro i à la lignePol"""
        self.__sommets.insert(i-1, p)
    
    def __str__ (self):
        txt = ""
        for x in range(len(self.__sommets)):
            txt = txt + str(self.__sommets[x]) + " "
        return txt

    def homothetie (self, k):
        for sommet in self.__sommets:
            sommet.homothetie(k)
    
    def translation (self, dx, dy):
        for sommet in self.__sommets:
            sommet.translation(dx, dy)
    
    def rotation (self, a):
        for sommet in self.__sommets:
            sommet.rotation(a)
    
    def tracer (self):
        """trace ma lignePol"""
        for i in range(len(self.__sommets)-1):
            tracerLigne(self.__sommets[i].x(), self.__sommets[i].y(),
                        self.__sommets[i+1].x(), self.__sommets[i+1].y())
        tracerLigne(self.__sommets[-1].x(), self.__sommets[-1].y(), self.__sommets[0].x(),
                    self.__sommets[0].y()) # trace la ligne entre le dernier et le premier point
    
def tracerLigne (x0, y0, x1, y1):
    """simule le tracé d'une ligne entre deux points (x0, y0) et (x1, y1) du plan"""
    print("tracé de (" + str(x0) + ", " + str(y0) + ") à (" + str(x1) + ", " + str(y1) + ")")


if __name__ == '__main__':
    point1 = Point(1, 2)
    print("Point 1: " + str(point1))
    point2 = Point (3, 3)
    print("Point 2: " + str(point2))
    point3 = Point (10,5)
    print("Point 3: " + str(point3))
    ligne = LignePol([point1, point2, point3])
    print("\nSommets de la ligne polygonale:")
    print(ligne)
    print("\nAJOUT DU POINT (2.0,2.0) en position 2.")
    point4 = Point(2, 2)
    ligne.setSommet(2, point4)
    print("\nSommets de la ligne polygonale:")
    print(ligne)
    print("\nTRACE DU POLYGONE:")
    ligne.tracer()