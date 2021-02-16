import math


def f14(n):
    if n == 0:
        return 5
    else:
        return 1/65*f14(n - 1) + math.sin(f14(n - 1))


# n = int(input())
# print(f"{f14(n):.2e}")
