class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # operator overloading 
    # https://www.programiz.com/python-programming/operator-overloading
    def __add__(self, another):
        return Vector2D(self.x + another.x, self.y + another.y)

    # __str__
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
    
    def display(self):
        print("x = {}, y = {}".format(self.x, self.y))

if __name__ == "__main__":
    print(" an instance with default value ".center(50, '-'))
    v0 = Vector2D()
    v0.display()

    print(" an instance with customized value ".center(50, '-'))
    v1 = Vector2D(3.3, 2)
    v1.display()

    v2 = Vector2D(4, 5)

    print(" added vector ".center(50, '-'))
    v_add = v1 + v0 + v2
    print(v_add.x, v_add.y)
    v_add.display()
    print(v_add)