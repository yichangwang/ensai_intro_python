class Rectangle:
    def __init__(self, length=30, width=15):
        self.length = length
        self.width = width
        self.nom = "rectangle"
    def surface(self):
        return self.length * self.width
    def __str__(self):
        return "The area of {} with length {} and width {} is {}".format(self.nom, self.length, self.width, self.surface())


class Square(Rectangle):
    def __init__(self, cote=10):
        Rectangle.__init__(self, cote, cote)
        self.nom = "square" # overload the attribute of an instance


if __name__ == '__main__':
    r = Rectangle(12, 8)
    print(r)
    c = Square()
    print(c)