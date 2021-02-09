import math


def function1_3(n, m):
    value1, value2 = 0
    for i in range(1, n):
        value1 += 25*i + math.exp(i)
    for i in range(1, n):
        for j in range(1, m):
            value2 = pow(i, 3) + pow(j, 4) + 82
    value = value1 - 2*value2
    return value


n = float(input())
m = float(input())
print(function1_3(m, n))
