def new_m(nr, nc):
    """Return an empty matrix of shape row x column"""
    m = {}
    for l in range(nr):
        for c in range(nc):
            m[(l, c)] = None
    return m


def set_m(m, i, j, x):
    m[(i, j)] = x


def get_m(m, i, j):
    cle = (i, j)
    if cle in m:
        return m[cle]
    else:
        return "index out of range"


if __name__ == "__main__":
    m = new_m(5, 4)
    print(m)
    set_m(m, 0, 0, 111)
    set_m(m, 1, 2, 222)
    set_m(m, 2, 1, 333)
    print(1, get_m(m, 3, 4))  # "index out of range"
    print(2, get_m(m, 3, 3))  # None
    print(3, get_m(m, 2, 1))  # 333