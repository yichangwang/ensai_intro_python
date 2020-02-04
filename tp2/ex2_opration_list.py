def transform(f, my_list):
    return [f(x) for x in my_list]


def filter(f, my_list):
    """ treat the elements from a list with the condition of f
    """
    return [x for x in my_list if f(x)]


if __name__ == "__main__":
    the_list = list(range(0, 6))  # [0, 1, 2, 3, 4, 5]
    print(transform(lambda x: x ** 2, the_list))  # [0, 1, 4, 9, 16, 25]
    print(filter(lambda x: x % 2 != 0, the_list))  # [1, 3, 5]
