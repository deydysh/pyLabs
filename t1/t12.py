import math


def f12(x):
    if x < -28:
        value = abs(pow(x, 7) + pow(x, 8)/22) + pow(x, 3)
    elif x < 69:
        value = 57*pow((pow(x, 8) + abs(x) - 35), 3) - math.exp(x)
    elif x < 134:
        value = 5*pow((pow(x, 6) - math.tan(x) + 17), 2) - pow(x, 6)/65
    elif x < 181:
        value = math.log(59*x) - math.exp(x)
    elif x >= 181:
        value = 81*pow((10*pow(x, 4) - math.cos(x) + 88), 6) - 55*pow(x, 4)
    return value


# n = int(input())
# print(f"{f12(n):.2e}")

