import random

names = ['Святослав', 'Доброжир', 'Тихомир', 'Ратибор', 'Ярополк', 'Гостомысл', 'Велимудр', 'Всеволод', 'Богдан',
         'Доброгнева', 'Любомила', 'Миролюб', 'Светозар', 'Милонег']
g = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
s = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'х', 'ц', 'ч', 'ш', 'щ']


def name_generator():
    f_name = names[random.randint(0, len(names) - 1)]
    l_name = s[random.randint(0, len(s) - 1)].upper()
    i = random.randint(4, 10)
    while i != 0:
        if i % 2 == 0:
            l_name += g[random.randint(0, len(g) - 1)]
        else:
            l_name += s[random.randint(0, len(s) - 1)]
        i -= 1
    return f_name + ' ' + l_name


print(name_generator())
print(name_generator())
print(name_generator())
