class Point:
    """classe des points du plan."""
    def __init__(self, x=0.0, y=0.0):
        self.px = float(x)
        self.py = float(y)


class Segment:
    """classe composite utilisant la classe Point."""
    def __init__(self, x1, y1, x2, y2):
        "L'initialisation utilise deux objets Point"
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def __str__(self):
        """Representation d'un objet segment."""
        return ("Segment : [({:.2f}, {:.2f}), ({:.2f}, {:.2f})]"
                .format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))


if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print(s)
