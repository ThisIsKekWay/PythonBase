# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
lst = [random.randint(1, 5) for n in range(random.randint(2, 10))]
res_lst = [n for n in lst if lst.count(n) == 1]

print(f'Начальный список: {lst}')
print(res_lst)

