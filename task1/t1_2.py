import math


def function1_2(x):
    if x < 85:
        value = 25*(math.cos(x) - 7*pow(x, 7)) + pow(x, 7)
    elif x < 110:
        value = pow(x, 4) + pow(x, 6)
    elif x < 186:
        value = 36*pow(x, 7) + pow(x, 5) - 84
    elif x < 202:
        value = pow((x - 41*pow(x,2)), 4) + math.tan(x)
    elif x >= 202:
        value = math.tan(x) + math.log(x)
    return value


x = float(input())
print("{:.2e}".format(function1_2(x)))
