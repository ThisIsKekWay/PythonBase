# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

a = int(input('Введите натуральное число '))

nums = []
div = 2
while a > 1:
    while a % div == 0:
        nums.append(div)
        a //= div
    div += 1
print(nums)
