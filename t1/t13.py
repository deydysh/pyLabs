import math


def f13(n):
    sum1, sum2 = 0, 0
    for i in range(1, n + 1):
        sum1 += 53*pow(i, 4) + math.tan(i)
    for j in range(1, n + 1):
        sum2 += 22*pow(j, 8) + 39*pow(j, 2)
    return sum1 - sum2


# n = int(input())
# print(f"{f13(n):.2e}")
