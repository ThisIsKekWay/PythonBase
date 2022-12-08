# Создайте программу для игры в ""Крестики-нолики""
import random

board = list(range(1, 10))
players = {1: 'X', 2: 'O'}

def print_board(brd):
    print("-" * 13)
    for i in range(3):
        print("|", brd[0 + i * 3], "|", brd[1 + i * 3], "|", brd[2 + i * 3], "|")
        print("-" * 13)


def check_win(desk):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            return desk[each[0]]
    return False


def sign_input(num, coord):
    if str(board[coord - 1]) not in 'XO':
        if num == 1:
            board[coord - 1] = 'X'
        else:
            board[coord - 1] = 'O'
    else:
        print('Введено неверное положение! Вы потеряли свой ход! ')


tour = random.randint(1, 2)
print('Первым ходит ' + players[tour])
last_tour = 0
counter = 0
while not check_win(board):
    print_board(board)
    if tour == 1:
        point = int(input('Игрок 1, ваш ход \n'
                          'Введите номер ячейки '))
        sign_input(tour, point)
        last_tour = tour
        tour = 2
    else:
        point = int(input('Игрок 2, ваш ход \n'
                          'Введите номер ячейки '))
        sign_input(tour, point)
        last_tour = tour
        tour = 1

    for i in board:
        if str(i) in 'XO':
            counter += 1
    if counter == 45:
        break

print_board(board)

if counter < 45:
    print(f'Игра окончена, победил игрок {last_tour}')
else:
    print('Ничья')
