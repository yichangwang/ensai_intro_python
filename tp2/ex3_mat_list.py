def new_m_shadow_copy(nr, nc):
    """Return an empty matrix of shape row x column"""
    r = [None] * nc
    return [r[:] for i in range(nr)]  # l[:] can be written as r.copy()


def new_m_reference(nr, nc):
    """Return an empty matrix of shape row x column"""
    r = [None] * nc
    # in this case, variable r is a reference of the list, change one element in
    # the matrix will change the element of every row
    # (each row points to the same list object)
    m = [r for i in range(nr)] 
    return m


def set_m(m, i, j, x):
    m[i][j] = x


def get_m(m, i, j):
    return m[i][j]


if __name__ == "__main__":
    m = new_m_shadow_copy(2, 3)
    print(m)
    set_m(m, 1, 2, 5)
    set_m(m, 0, 1, 6)
    print(m)

    m2 = new_m_reference(2, 3)
    print(m)
    set_m(m, 1, 2, 5)
    set_m(m, 0, 1, 6)
    print(m)
