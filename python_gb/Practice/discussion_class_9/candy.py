from random import randint, choice


def turn_player(candys, player=''):
    print('Ходит игрок', player)
    take_candys = int(input('Сколько конфет вы возьмёте? (1-28) :'))
    if take_candys > candys:
        take_candys = candys
    candys -= take_candys
    print(candys)
    print(f'Игрок {player} взял {take_candys} конфет.')
    return candys


def turn_computer(candys, difficulty=False):
    print('Ходит компьютер')
    if difficulty:
        computer = candys % 29
    else:
        computer = randint(1, 28)
    if computer > candys:
        computer = candys
    print(f'Компьютер взял {computer} конфет.')
    candys -= computer
    return candys


def move(candys, player, difficulty=False):
    if player == 'игрок':
        return turn_player(candys)
    else:
        return turn_computer(candys, difficulty)


def game_players(rest_candys):
    num_player = 1
    rest_candys = turn_player(rest_candys, num_player)
    while rest_candys > 0:
        print(f'Осталось {rest_candys} конфет')
        num_player = 3 - num_player
        rest_candys = turn_player(rest_candys, num_player)
    return num_player


def game_bot(rest_candys, difficulty=False):
    variants = ('игрок', 'компьютер')
    player = choice(variants)
    rest_candys = move(rest_candys, player, difficulty)
    while rest_candys > 0:
        print(f'Осталось {rest_candys} конфет')
        player = variants[1 - variants.index(player)]
        rest_candys = move(rest_candys, player, difficulty)
    return player


def main():
    rest_candys = 2021
    game = input('Выберите вариант игры: 1, 2 или 3:\n\
                 1 - Игрок против игрока\n\
                 2 - Игрок против компьютера\n\
                 3 - Игрок против умного компьютера.\n')
    if game == '1':
        print(f'Победил {game_players(rest_candys)} игрок.')
    elif game == '2':
        print(f'Победил {game_bot(rest_candys)}.')
    else:
        print(f'Победил {game_bot(rest_candys, True)}.')


if __name__ == '__main__':
    main()