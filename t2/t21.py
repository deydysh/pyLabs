def f21(x):
    if x[3] == 'rexx':
        if x[0] == 1977:
            if x[2] == 'grace':
                return 0
            elif x[2] == 'fancy':
                return 1
            elif x[2] == 'flux':
                return 2
        elif x[0] == 2007:
            if x[1] == 'gams':
                return 3
            elif x[1] == 'e':
                return 4
            elif x[1] == 'lsl':
                return 5
    elif x[3] == 'dylan':
        return 6
    elif x[3] == 'sage':
        if x[1] == 'gams':
            return 7
        elif x[1] == 'e':
            if x[2] == 'grace':
                return 8
            elif x[2] == 'fancy':
                return 9
            elif x[2] == 'flux':
                return 10
        elif x[1] == 'lsl':
            return 11


print(f21([1977, 'e', 'fancy', 'rexx']))
print(f21([1977, 'e', 'grace', 'sage']))
