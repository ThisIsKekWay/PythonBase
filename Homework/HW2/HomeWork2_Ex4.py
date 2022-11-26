f = open("file.txt")

num = int(input('Введите число '))
li = []

for i in range(-num, num + 1):
    li.append(i)

print(li)

res = 1
for j in range(1, 4):
    n = int(f.read(j))
    print(f'Позиция списка из фалйа {n}')
    res *= li[n]

print(res)
