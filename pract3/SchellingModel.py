from random import randint
import matplotlib.pyplot as plt


class Agent:
    def __init__(self, type):
        self.type = type  # Группа агента
        self.location = -1, -1  # Локация при инициализации объекта
        self.set_location()

    def __str__(self):
        return f"Agent({self.type})"

    def __repr__(self):
        return f"Agent({self.type})"

    def set_location(self):
        if self.location != (-1, -1):  # Сюда попадаем, если функция вызывается не в первый раз
            grid[self.location[0]][self.location[1]] = 0  # Убираем агента с сетки
        flag = True
        while flag:  # Пока не найдем свободное место
            i, j = randint(0, grid_size - 1), randint(0, grid_size - 1)  # Генерируем случайную пару чисел
            if grid[i][j] == 0:  # Нашли пустое место
                grid[i][j] = self  # Добавляем агента на сетку
                self.location = i, j  # Кортеж с локацией агента на сетке
                flag = False

    def distance(self, other):
        # Вычисляем манхэттенское расстояние
        return abs(self.location[0] - other.location[0]) + abs(self.location[1] - other.location[1])

    def is_happy(self, agents):
        # Возвращает True, если среди соседей достаточное кол-во агентов той же группы

        distances = []  # Лист пар (d, agent), d - дистанция от self до agent
        for agent in agents:
            if self != agent:
                distance = self.distance(agent)
                distances.append((distance, agent))
        distances.sort(key=lambda x: x[0])  # Сортируем от меньшему к большему, учитывая расстояние
        neighbours = [agent for d, agent in distances[:num_neighbours]]  # Список ближайших num_neighbours агентов
        num_same_type = sum(self.type == agent.type for agent in neighbours)  # Кол-во агентов той же группы
        return num_same_type >= require_same_type

    def update_location(self, agents):
        # self.set_location()
        while not self.is_happy(agents):
            self.set_location()


def plot_distribution(agents, cycle_num):
    x_values_1, y_values_1 = [], []
    x_values_2, y_values_2 = [], []
    for agent in agents:
        x, y = agent.location
        if agent.type == 1:
            x_values_1.append(x)
            y_values_1.append(y)
        if agent.type == 2:
            x_values_2.append(x)
            y_values_2.append(y)
    fig, ax = plt.subplots()
    plot_args = {'markersize': 10, 'alpha': 0.6}
    ax.set_facecolor('azure')
    ax.plot(x_values_1, y_values_1, 'o', markerfacecolor='blue', **plot_args)
    ax.plot(x_values_2, y_values_2, 'o', markerfacecolor='red', **plot_args)
    ax.set_title(f'Cycle {cycle_num}')
    plt.show()


# Main #
num_neighbours = 10  # Число близжайших агентов, которые считаются соседями

print("Введите пороговую толерантность в %")
tolerance = int(input())

print("Введите суммарное количество агентов")
population = int(input())

print("Введите % агентов, относящихся к первой группе")
f_percent = int(input())

print("Введите % агентов, относящихся ко второй группе")
s_percent = int(input())

print("Введите размер сетки")
grid_size = int(input())

print("Введите количество шагов симуляции")
num_steps = int(input())


f_population = population*f_percent//100  # Количесвто агентов первой группы
s_population = population*s_percent//100  # Количесвто агентов второй группы
require_same_type = num_neighbours * tolerance // 100  # Пороговое количесвто соседей

grid = [[0]*grid_size for i in range(grid_size)]  # Создаем двумерный массив нулей размером grid_size X grid_size

agents = [Agent(1) for i in range(f_population)]  # Добавляем на сетку агентов первой группы
for i in range(s_population):  # Второй группы
    agents.append(Agent(2))

count = 0  #
while count != num_steps:
    plot_distribution(agents, count)
    for agent in agents:
        agent.update_location(agents)
    count += 1

