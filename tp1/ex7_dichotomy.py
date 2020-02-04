def solution(f, a, b, epsilon):
    """Calculate the root of monotone function by bisection method
    on the interval [a, b] 
    f: function (float -> float)
    a, b: float
    epsilon: float
    """
    while abs(a - b) > epsilon:
        c = (a + b) / 2.0
        yc = f(c)
        ya = f(a)
        if yc * ya > 0.0:
            a = c
        else:
            b = c
    return a

if __name__ == '__main__':
    print("test:")
    print(solution(lambda x: x-1, 0.5, 1.5, 1e-8))
