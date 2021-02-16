import math


def function1_1(x, y, z):
    return (25*z + math.exp(z))/(pow(z, 8) - x)\
           - (abs(pow(x, 5) - 46*pow(x, 8)) - 13*pow(x, 6))\
           - math.sqrt((90*z + pow(x, 3))/((pow(z, 6)/45) + 8*pow(y, 5) - 2))



x = float(input())
y = float(input())
z = float(input())
print("{:.2e}".format(function1_1(x, y, z)))
