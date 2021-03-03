def f6(s):
    return sorted(s, key=lambda x: len(x))[len(s)-1]


print(f6(['aaaaaa', 'aa', 'aaaaaaaaaaa']))
