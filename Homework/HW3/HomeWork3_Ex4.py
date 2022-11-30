# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
num = int(input('Введите число '))
lst = [0, 1]

for i in range(num - 1):
    lst.append(lst[i] + lst[i + 1])

lst.insert(0, 1)

for j in range(num - 1):
    lst.insert(0, (lst[1] - lst[0]))
print(lst)
