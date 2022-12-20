# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# *Пример:*
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
Словарь – самый простой пример – телефонная книжка
my_dict = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
1) все ключи уникальны
2) ключами могут быть только неизменяемые типы данных
3) значениями могут быть любые типы данных
4) неупорядоченные
5) чтобы пееревести в словарь есть функция dict() – словарь
list() – список
Вложенные списки легко преобразовывать в словарь:
my_list = [[4, 13], [5, 16]] – длина списка должна быть не более 2 элементов
new_dict = dict(my_list)
'''
from os import *
system('cls')


number = int(input("Enter a value: "))
my_list = []

for i in range(1, number + 1):
    my_list.append([i, 3 * i + 1])
print(dict(my_list))
