# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

num = int(input('Введите число '))
dct = {}
sum = 0
for i in range(1, num + 1):
    dct[i] = round(((1 + (1/i)) ** i), 2)
    sum += dct[i]
print(dct, sum)
