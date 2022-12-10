# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

my_str1 = input('Введите пример: ').split()


def prod_div(my_str):
    while '*' in my_str or '/' in my_str:
        try:
            prod_index = my_str.index('*')
        except:
            prod_index = 1000

        try:
            div_index = my_str.index('/')
        except:
            div_index = 1000

        if prod_index < div_index:
            my_str[prod_index - 1] = int(my_str[prod_index - 1]) * int(my_str[prod_index + 1])
            my_str.pop(prod_index + 1)
            my_str.pop(prod_index)
        else:
            my_str[div_index - 1] = int(my_str[div_index - 1]) / int(my_str[div_index + 1])
            my_str.pop(div_index + 1)
            my_str.pop(div_index)

    return my_str


def sum_deg(my_str):
    while '+' in my_str or '-' in my_str:
        try:
            sum_index = my_str.index('+')
        except:
            sum_index = 1000

        try:
            deg_index = my_str.index('-')
        except:
            deg_index = 1000

        if sum_index < deg_index:
            my_str[sum_index - 1] = int(my_str[sum_index - 1]) + int(my_str[sum_index + 1])
            my_str.pop(sum_index + 1)
            my_str.pop(sum_index)
        else:
            my_str[deg_index - 1] = int(my_str[deg_index - 1]) - int(my_str[deg_index + 1])
            my_str.pop(deg_index + 1)
            my_str.pop(deg_index)

    return my_str


def fancy_moves(my_str):
    while '(' in my_str:
        open_sign = 0
        os1 = my_str.index('(')
        close_sign = my_str.index(')')
        try:
            os2 = my_str[os1 + 1::].index('(') + os1 + 1
        except:
            os2 = os1
        if os2 > close_sign:
            open_sign = os1
        else:
            open_sign = os2

        ls1 = my_str[open_sign + 1: close_sign]

        my_str[open_sign + 1] = prod_div(ls1)[0]
        my_str[open_sign + 1] = sum_deg(ls1)[0]

        while my_str[open_sign + 2] != ')':
            my_str.pop(open_sign + 2)
        my_str.pop(open_sign + 2)
        my_str.pop(open_sign)


    return my_str


while len(my_str1) != 1:
    fancy_moves(my_str1)
    prod_div(my_str1)
    sum_deg(my_str1)

print(my_str1)
