a = float(input())
b = float(input())
i = 1

print("{}-й день: {:.2f}".format(i, a))
while a < b:
    i += 1
    a *= 1.1
    print("{}-й день: {:.2f}".format(i, a))
