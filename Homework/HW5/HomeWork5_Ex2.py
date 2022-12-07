# Игра с конфетами. Дано 2021 конфет.
# Каждый игрок за каждый ход может взять не более 28 конфет.
# Побеждает игрок,забравший последнюю конфету.
# Сколько конфет надо взять первому игроку, чтобы победить?

import random
candies = 2021
borders = [1, 28]
players = {1: 'Бот', 2: 'Игрок'}
print('Начинается против бота-тупня! \n'
      'Определяем, кто пойдет первым! \n')

tour = random.randint(1, 2)
print('Первым ходит ' + players[tour])

while candies != 0:
    print(f'Остаток конфет {candies}\n'
          'Ходит' + players[tour])
    if tour == 1:
        take = random.randint(1, 28)
        if take > candies:
            take = random.randint(1, candies)
        else:
            print(f'Бот взял {take}')
            candies -= take
            if candies != 0:
                tour = 2
    else:
        take = int(input('Игрок, ваша очередь брать конфеты! \n'
                         'Вы берете: '))
        if take > candies or take > 28 or take < 1:
            print('Игрок, вы не можете взять столько конфет, ваш ход переходит Боту')
            tour = 1
        else:
            candies -= take
            if candies != 0:
                tour = 1
print('Все конфеты кончились, победил ' + players[tour])
