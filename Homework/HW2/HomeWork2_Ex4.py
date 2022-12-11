

num = int(input('Введите число '))
li = [n for n in range(-num, num + 1)]

print(li)

res = 1
with open("file.txt", 'r') as f:
    for j in range(1, 4):
        n = int(f.read(j))
        print(f'Позиция списка из файла {n}')
        res *= li[n]

print(res)
