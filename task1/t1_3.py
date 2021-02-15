import math


def function1_3(n, m):
    value1, value2 = 0, 0
    for i in range(1, n+1):
        value1 += 25*i + math.exp(i)
    for j in range(1, n+1):
        for k in range(1, m+1):
            value2 += pow(j, 3) + pow(k, 4) + 82
    value = value1 - 2*value2
    return value


n = int(input())
m = int(input())
print("{:.2e}".format(function1_3(n, m)))
