# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def add_ratio(poly):
    poly.insert(0, '0')
    poly.insert(2, '1')
    return poly

def add_zeroes(poly1, poly2):
    if len(poly1) > len(poly2):
        for i in range((len(poly1) - len(poly2)) // 2):
            poly2.append(str(len(poly2) // 2))
            poly2.append('0')
    else:
        for i in range((len(poly2) - len(poly1)) // 2):
            poly1.append(str(len(poly1) // 2))
            poly1.append('0')


def realise_poly(poly):
    res_str = ''
    k = len(poly) - 1
    x = 1
    y = 1
    j = 0
    while k != -1:
        if k <= 1:
            x = 0
        if k == 0:
            y = 0
        res_str += str('{:+}'.format(poly[j])) + y * ('x' + x * ('^' + str(k)) + ' ')
        k -= 1
        j += 1
    res_str += ' = 0'
    return res_str


with open('HW4_4.txt', 'r') as f:
    str1 = f.readline().strip()
    str2 = f.readline().strip()

res_lst = []

main_str1 = str1.split(' = ')[0]
main_str2 = str2.split(' = ')[0]

main_str1 = main_str1.replace('x', '').replace('^', ' ')
main_str2 = main_str2.replace('x', '').replace('^', ' ')

lst1 = main_str1.split()
lst2 = main_str2.split()

lst1.reverse()
lst2.reverse()

add_ratio(lst1)
add_ratio(lst2)

add_zeroes(lst1, lst2)
print(lst1)
print(lst2)
for i in range(0, len(lst1), 2):
    res_lst.append(int(lst1[i + 1]) + int(lst2[i + 1]))

res_lst.reverse()

res_str = realise_poly(res_lst)
with open('HW4_5.txt', 'a') as f:
    if res_str[0] == '+':
        f.write(res_str[1:])
        f.write('\n')
    else:
        f.write(res_str)
        f.write('\n')

