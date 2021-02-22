t21 = [
    ([1994, 1963, 1962, 'xproc', 'xbase'], 8),
    ([1994, 1963, 2003, 'rexx', 'max'], 7),
    ([1994, 2011, 2003, 'xproc', 'max'], 8),
    ([1994, 1963, 1962, 'rexx', 'max'], 2),
    ([2012, 2011, 2003, 'xproc', 'xbase'], 8),
    ([1994, 2011, 2003, 'xproc', 'xbase'], 8),
    ([2012, 2011, 2003, 'xproc', 'max'], 8),
    ([2012, 2011, 2003, 'rexx', 'max'], 5),
    ([2012, 2011, 1962, 'xproc', 'max'], 8),
    ([1994, 1963, 2003, 'rexx', 'xbase'], 7)
]


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


for i in range(len(t21)):
    if f21(t21[i][0]) == t21[i][1]:
        print(f"Тест {i} пройден [{f21(t21[i][0])}]")
    else:
        print(f"Ошибка в тесте {i}")
