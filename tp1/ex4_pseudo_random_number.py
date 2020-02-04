import math
import random


def compute_mean_and_stdev(n):
    """n: int, draw number
    return: mean and stdev value of the series
    """
    sum = 0
    sum_squared_x = 0

    for i in range(n):
        x = random.random() # float number in [0, 1[
        sum += x # sum +=x  <=> sum = sum + x
        sum_squared_x += x * x
    mean = sum / n # ~0.5
    stdev = math.sqrt(sum_squared_x / n - mean * mean) # ~1/sqrt(12)
    return mean, stdev

def dna_series(n):
    dna = []
    for i in range(n):
        temp = random.randint(0, 3)
        dna.append('actg'[temp])
    return "".join(dna)
    
    
if __name__ == "__main__":
    print(compute_mean_and_stdev(100000))
    print(dna_series(10))