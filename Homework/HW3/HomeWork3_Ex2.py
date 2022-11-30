# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

lst = list()

# Задание списка
for i in range(random.randint(2, 6)):
    lst.append(round(random.uniform(-10, 10), 2))
print(lst)

# Блок изменения списка
for i in range(len(lst)):
    lst[i] = round(lst[i] - int(lst[i]), 2)
print(lst)

# Вычисление разницы
print(round(max(lst) - min(lst), 2))
