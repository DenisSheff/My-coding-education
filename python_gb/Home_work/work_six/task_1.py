from random import randint


def multiply_odds():
    my_block = [i for i in range(randint(1, 10))]
    index_counter = 0
    for i in range(len(my_block)):
        if i % 2 != 0:
            index_counter += my_block[i]
    print(my_block)
    print(index_counter)


multiply_odds()
