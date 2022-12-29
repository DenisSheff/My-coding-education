# 1. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

list_number = input("Enter values using space: ").split()
for i in range(len(list_number)):
    list_number[i] = int(list_number[i])
print(list_number)
print(max(list_number))
print(min(list_number))


