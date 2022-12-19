# . Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23

# - 0,56 -> 11

number = float(input("Enter a value: "))
sum = 0


while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print(f"The sum of all digits is {int(sum)}.")
