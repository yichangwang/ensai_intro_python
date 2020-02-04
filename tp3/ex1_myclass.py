class MyClass:
    """my class object"""
    x = 23
    y = x + 5
    
    def __init__(self, z=42):
        self.z = z
    
    def display(self):
        print("y = {}, z = {}".format(self.y, self.z))


if __name__ == "__main__":
    c = MyClass(3)
    c.y = 10
    # MyClass.y = 30
    MyClass.display(c)
    c.display()
    print(c.y)

    d = MyClass(4)
    d.display()
    print(d.y)
