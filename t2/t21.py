def f21(x):
    if x[3] == 'rexx':
        if x[2] == 1962:
            if x[1] == 2011:
                return 0
            elif x[1] == 1963:
                if x[4] == 'xbase':
                    return 1
                elif x[4] == 'max':
                    return 2
        elif x[2] == 1987:
            return 3
        elif x[2] == 2003:
            if x[1] == 2011:
                if x[4] == 'xbase':
                    return 4
                elif x[4] == 'max':
                    return 5
            elif x[1] == 1963:
                if x[0] == 2012:
                    return 6
                elif x[0] == 1994:
                    return 7
    elif x[3] == 'xproc':
        return 8


# a = [int(input()), int(input()), int(input()), input(), input()]
# print(f21(a))
