# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input("Enter a number: "))

if 6 <= day_number <= 7:
    print("Yes, it is a day-off! Enjoy :)")
else:
    print("No! Get back to work!")