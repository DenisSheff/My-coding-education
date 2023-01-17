from random import randint


def pick_candy(gamer):
    candy_amount = int(input(f"{gamer}, enter amount of 🍬's from 1 to 28 you are going to pick up: "))
    while 1 > candy_amount > 28:
        candy_amount = int(input("Pay attention! You need to choose 🍬 in range from 1 to 28. Try again."))
    return candy_amount


def print_gamer_move(gamer, candy_counter, result_counter, table_value):
    print(f"{gamer} made a move. Now {gamer} picked up {candy_counter} candies."
          f" {gamer} has {result_counter}. {table_value} of candies have left on the table.")


def main():
    player_1 = input("Enter a name of the first gamer: ")
    player_2 = input("Enter a name of the second gamer: ")
    table_value = int(input("Enter amount of candies for the game: "))
    game_order = randint(0, 2)
    counter_player_1, counter_player_2 = 0, 0
    print()
    print('Rules:')
    print(f'There are {table_value} candies on the table. Two players make a move one after another.'
          f'\nFirst move will be chosen randomly. For one move you can not pick up more than 28 candies.'
          f'\nThe one who won will get all the candies.'
          f'\nLet the battle begin!')
    print()
    if game_order:
        print(f"{player_1} makes first move.")
    else:
        print(f"{player_2} makes first move.")
    print()
    while table_value > 28:
        if game_order:
            candy_counter = pick_candy(player_1)
            counter_player_1 += candy_counter
            table_value -= candy_counter
            game_order = False
            print_gamer_move(player_1, candy_counter, counter_player_1, table_value)
        else:
            candy_counter = pick_candy(player_2)
            counter_player_2 += candy_counter
            table_value -= candy_counter
            game_order = True
            print_gamer_move(player_2, candy_counter, counter_player_2, table_value)
    if game_order:
        print(f'{player_1} won.')
    else:
        print(f'{player_2} won.')


if __name__ == "__main__":
    main()
