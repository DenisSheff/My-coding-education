from random import *


def fill_array(elements, new_block):
    for _ in range(elements):
        new_block.append(randint(-elements, elements))
    return new_block
