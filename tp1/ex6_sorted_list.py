def uniq(my_list):
    """Eliminate redundant elements in the list and sort the list
    my_list: list with numbers inside
    """
    my_set = set(my_list)
    new_list = list(my_set)
    return sorted(new_list)


def fusion(list1, list2):
    """Merge two list, eliminate redundant elements in the merged list, then 
    return sorted list
    list1, list2: two list with numbers inside
    """
    my_set = set(list1 + list2)
    new_list = list(my_set)
    return sorted(new_list)


if __name__ == "__main__":
    print(uniq([2, 1, 3, 3, 8, 0, 7, 4]))
    print(fusion([2, 1, 3, 3, 8, 0, 7, 4], [2, 9, 6, 5, 10, 12, 11, 21, 12]))
