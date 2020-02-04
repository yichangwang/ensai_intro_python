from ex1_position import position


def sub_list(small_list, big_list):
    """ Return True if small list is in the big list
    """
    p = -1
    for c in small_list:
        p = position(c, big_list, p+1)
        if p == -1:
            return False
    return True


if __name__ == "__main__":
    bl = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(1, sub_list([ 2, 4, 12, 20 ], bl))
    print(2, sub_list([], bl))
    print(3, sub_list(bl, bl))
    print(4, not sub_list([ 2, 4, 12, 6, 20 ], bl))
    print(5, sub_list((2, 4, 6), (1, 2, 3, 4, 5, 6)))
    print(6, not sub_list((2, 4, 6), (1, 2, 3, 4, 5)))
    print(7, sub_list("bdfh", "abcdefghi"))
    print(8, not sub_list("bdfh", "acdefghi"))
