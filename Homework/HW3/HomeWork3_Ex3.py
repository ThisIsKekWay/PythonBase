# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число '))
ans = ''
remain = 0

while num > 0:
    remain = num % 2
    num //= 2
    ans = ans + str(remain)

print(ans[::-1])
