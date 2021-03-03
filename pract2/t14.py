def f4(x, s):
    return [i for i in range(len(s)) if s[i] == x]


print(f4(3, [3, 0, 0, 3, 1, 3, 4]))
