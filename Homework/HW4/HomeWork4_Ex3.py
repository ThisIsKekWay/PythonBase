# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
lst = []
res_lst = []

for i in range(random.randint(2, 10)):
    lst.append(round(random.randint(1, 5), 2))
print(f'Начальный список: {lst}')

for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        res_lst.append(lst[i])
print(res_lst)
