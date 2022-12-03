# input_str = input('Введите числа через пробел ')
#
# lst = input_str.split()
#
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
#
# print(max(lst), min(lst))


str = '-5x^2 - 9x + 3 = 0'
print(str)
main_str = str.split(' = ')[0]
print(main_str)
# a, b, c = main_str.split(' + ')

a, lit1, b, lit2, c = main_str.split()
b = lit1 + b
c = lit2 + c
a = int(a[:a.index('x')])
b = int(b[:b.index('x')])
c = int(c)
print(a)
print(b)
print(c)

D = b ** 2 - 4 * a * c
print(D)
if D < 0:
    print('корней нет')
elif D == 0:
    print(f'x = {-b/(2 * a)}')
else:
    print(f'x1 = {round((-b + (D ** 0.5)) / (2 * a), 2)}')
    print(f'x2 = {round((-b - (D ** 0.5)) / (2 * a), 2)}')
#
# lst = [int(i) for i in input('Введите числа через пробел ').split()]  # Задаем список
# a = lst[0]
# b = lst[1]
# print(a, b)
#
# if lst[0] < lst[1]:
#     c = lst[0]
#     lst[0] = lst[1]
#     lst[1] = c
#
# while lst[1] != 0:
#     c = lst[0] % lst[1]
#     lst[0] = lst[1]
#     lst[1] = c
#
# print(f'НОД = {lst[0]}, НОК = {(a * b) // lst[0]}')
