def power_of_two_inf(k):
    p = 1
    iter_number = 0
    while p <= k:
        iter_number += 1
        p = 2 * p
    return p / 2, iter_number


if __name__ == "__main__":
    val = 5
    p, iter_nb = power_of_two_inf(2)
    print("p: {} at iter {}".format(p, iter_nb))
