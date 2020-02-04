def include(a, b):
    """Test if every letter in a is from b
    a, b: strings to compare

    returns: True if every letter of a appears in b, False otherwise
    """
    for c in a:
        if c not in b:
            return False
    else:
        return True


def verify_integer_positive(val):
    """Verify if the value is a positive number
    val: string
    """
    return len(val)>=1 and include(val, "0123456789")


def verify_integer_relative(val):
    """verify if the value is a positive int or negative int
    val: string
    """
    return verify_integer_positive(val) or \
            (val[0]=='-' and verify_integer_positive(val[1:]))


def verify_integer_valid(val, inf=None, sup=None):
    """verify if val is a int number, and
    when the interval is specified verify it is in the interval
    
    val, inf, sup: strings
    inf: infimum (default None); sup: supremum (default None)
    """
    return verify_integer_relative(val) and (inf==None or int(val)>=inf) and \
        (sup==None or int(val)<=sup)


if __name__ == "__main__":
    number = 30
    val = str(number)
    print(verify_integer_valid(val+'.5'))  # False
    print(verify_integer_valid(val))  # True
    print(verify_integer_valid(val, 20, 40))  # True
    print(verify_integer_valid(val, 35, 40))  # False
