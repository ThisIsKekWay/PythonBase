# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

lst = list()

for i in range(random.randint(2, 6)):
    lst.append(random.randint(-10, 10))
print(lst)

res_lst = list()
j = -1
if len(lst) % 2 != 0:
    size = int(len(lst) / 2) + 1
else:
    size = int(len(lst) / 2)

for i in range(size):
    res_lst.append(lst[i] * lst[j])
    j -= 1
print(res_lst)

