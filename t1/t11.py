import math


def f11(x, y, z):
    return math.sqrt(53*pow(z, 4) + math.tan(x))\
           - (pow(y, 7) - 57*pow(x, 3))\
           + abs(abs(x) - 99*pow(z, 8))\
           + pow(x, 5)
