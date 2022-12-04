# def f(x):
#     return x**2
#
# g = f
# print(f(2))
# print(g(2
#
# def calc(x):
#     return x + 10
#
# def calc2(x):
#     return x * 10
#
# def math(op,x):
#     print(op(x))
#
# math(calc, 10)
# math(calc2, 10)
#
# def sum(x, y):
#     return x + y
#
# sum = lambda x, y: x + y + 1
#
# def mlt(x, y):
#     return x * y
#
# def calc(op, a, b):
#     print(op(a, b))
#     return op(a, b)
#
# calc(lambda x, y: x + y, 4 , 5)

# list = []
#
# for i in range(21):
#     if i % 2 == 0:
#         list.append(i)
#
# print(list)

# def f(x):
#     return x ** 2
#
#
# lst = [1, 2, 3, 5, 8, 15, 23, 38]
#
# list = [(i, f(i)) for i in lst if i % 2 == 0]
# print(list)

#

# data = '1 2 3 5 8 15 23 38'.split()
# print(data)
# res = list(map(int, data))
# print(res)
# res = list(filter(lambda x: not x % 2, res))
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# li = [x for x in range(1, 20)]
#
# print(li)
#
# li = list(map(lambda x: x + 10, li))
#
# print(li)

# data = [x for x in range(10)]
# res = list((filter(lambda x: not x % 2, data)))
# print(res)

users = ['user1', 'user2', 'user3', 'user4']
ids = [4, 5, 9, 5, 7]

data = list(enumerate(users))
print(data)