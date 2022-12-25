# 4. Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input("Enter a value for a number: "))
new_number = ''
while number != 0:
    new_number = str(number % 2) + new_number
    number //= 2
print(new_number)
