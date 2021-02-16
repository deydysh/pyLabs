earnings = float(input())
costs = float(input())

if earnings > costs:
    print("Компания работает в плюс")
    print("Рентабельность: {}".format((earnings - costs)/earnings))
    print("Введите численность сотрудников: ")
    stuff = int(input())
    print("Прибыль фирмы в рассчете на одного сотрудника: {}".format((earnings - costs)/stuff))
else:
    print("Компания работает в минус")
