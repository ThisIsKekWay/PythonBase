# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('before.txt', encoding='utf-8', mode='r') as f:
    str1 = f.read()
print('Начальная строка: ' + str1)


def code_str(s):
    coded_str = ''
    counter = 0
    init_char = str1[0]
    for char in s:
        if char == init_char:
            counter += 1
        else:
            coded_str += str(counter) + init_char
            init_char = char
            counter = 1
    return coded_str


print('Закодированная строка: ' + code_str(str1))

with open('after.txt', 'a') as f:
    f.write(code_str(str1))

with open('after.txt', 'r') as f:
    str2 = f.read()

def decode_str(st):
    count = ''
    str_decode = ''
    for char in st:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


print('Декодированная строка: ' + decode_str(str2))
