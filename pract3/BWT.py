def cycle_move(s):
    # for i in range(len(s) - 1):
    return s[len(s)-1] + s[:len(s)-1]


def bwt_coding(s):
    lst = []
    tmp = ''
    s1 = s
    for i in range(len(s)):
        lst.append(s)
        s = cycle_move(s)
    lst.sort()
    for i in range(len(lst)):
        if s1 == lst[i]:
            index = i
    for item in lst:
        tmp += item[len(item)-1]
    return tmp, index


def bwt_decoding(s, index):
    lst = list(s)
    for i in range(len(s) - 1):
        lst.sort()
        for j in range(len(lst)):
            lst[j] = s[j] + lst[j]
            print(lst)
    lst.sort()
    return lst[index]



print(bwt_coding('ABACABA'))
print(bwt_decoding('BCABAAA', 2))
