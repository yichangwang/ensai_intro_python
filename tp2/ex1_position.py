def position(elt, my_list, start):
    """ return the index of the element in the list after start position
    -1 if element is absent
    """
    for i in range(start, len(my_list)):
        if elt == my_list[i]:
            return i
    return -1


if __name__ == "__main__":
    gl = [2, 4, 6, 2, 10, 12, 2, 16, 18, 20]
    print(1, position( 2, gl, 0) == 0)
    print(2, position( 2, gl, 4) == 6)
    print(3, position( 2, gl, 8) == -1)
    print(4, position( 3, gl, 0) == -1)
