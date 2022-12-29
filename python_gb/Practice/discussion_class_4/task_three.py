# 3. Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


number_1 = int(input("Enter a value for 'A': "))
number_2 = int(input("Enter a value for 'B': "))
max_number = max(number_1, number_2)
min_number = min(number_1, number_2)
for num in range(max_number, number_1 * number_2 + 1, max_number):
    if num % min_number == 0:
        print(num)
        break
