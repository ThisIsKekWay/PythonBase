# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k(до 6 степени).
import random

k = int(input('Введите порядок многочлена '))
ratios = []
res_str = ''

for i in range(k + 1):
    ratios.append('{:+}'.format(random.randint(-10, +10)))
    

x = 1
y = 1
j = 0
while k != -1:
    if k <= 1:
        x = 0
    if k == 0:
        y = 0
    res_str += ratios[j] + y * ('x' + x * ('^' + str(k)) + ' ')
    k -= 1
    j += 1

res_str += ' = 0'
with open('HW4_4.txt', 'a') as f:
    if res_str[0] == '+':
        f.write(res_str[1:])
        f.write('\n')
    else:
        f.write(res_str)
        f.write('\n')
