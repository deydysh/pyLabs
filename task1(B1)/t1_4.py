import math


def function1_4(n):
    if n == 0:
        return 7
    else:
        return math.tan(function1_4(n-1)) - math.cos(function1_4(n-1))


n = int(input())
print("{:.2e}".format(function1_4(n)))
