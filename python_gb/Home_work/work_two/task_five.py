# Реализуйте алгоритм перемешивания списка.
from random import *

number = int(input("Enter an amount of elements in the list: "))
new_list = []

for _ in range(number):
    new_list.append(randrange(-100, 100))

print(f"Created list --> {new_list}. Mixed list --> {shuffle(new_list)}.")
