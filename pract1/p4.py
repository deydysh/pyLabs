def maximum_digit(n):
    maximum = -1
    while n > 0:
        if n % 10 > maximum:
            maximum = n % 10
        else:
            n //= 10
    return maximum


n = int(input())
print(maximum_digit(n))
