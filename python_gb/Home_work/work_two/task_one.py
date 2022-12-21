# . Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23

# - 0,56 -> 11

number = input("Enter a value: ")
sum_of_digits = 0

for i in number:
    if i.isdigit():
        sum_of_digits += int(i)
print(f"The sum of all digits is {sum_of_digits}.")
