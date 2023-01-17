import os
from random import choice, randint


def start_game():
    print("Да начнется ИГРА!")
    print("=================")
    print("Правила:")
    print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
        \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \
        \nВсе конфеты оппонента достаются сделавшему последний ход.")
    print()
    print("Определяем очередность ходов: Введите 0 - если выбираете ОРЁЛ, 1 - если РЕШКА")
    mychoice = int(input())
    chance = choice([0, 1])
    print("Выпала РЕШКА") if chance else print("Выпал ОРЁЛ")
    if mychoice == chance:
        print("Вы ходите первым")
        return True
    else:
        print("Вы ходите вторым")
        return False


def player_turn():
    print("Введите количество взятых конфет (не более 28)")
    turn = 50
    while turn > 28:
        turn = int(input())
    return turn


def ai_turn():
    turn = 2023
    while turn > candies:
        if candies <= 28:
            turn = candies
        else:
            # turn = randint(1,28)
            turn = candies % 29 if candies % 29 != 0 else randint(1, 28)
    print("ПК взял", turn, "конфет")
    return turn


def print_candies():
    print()
    print("Количество оставшихся конфет:", candies)
    return


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if start_game():
        player_first = True
    else:
        player_first = False

    global candies
    candies = 200
    win = ""

    while candies > 1:
        print_candies()

        if player_first:
            candies -= player_turn()
            if candies == 0:
                win = "Игрок"
                break
            candies -= ai_turn()
            if candies == 0:
                win = "Компьютер"
                break
        else:
            candies -= ai_turn()
            if candies == 0:
                win = "Компьютер"
                break
            print_candies()
            candies -= player_turn()
            if candies == 0:
                win = "Игрок"
                break
    print("Выиграл", win)


if __name__ == "__main__":
    main()