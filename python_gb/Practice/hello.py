# # # Задачи:

# # # 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# # # *Примеры:*

# # # - 5, 25 -> да
# # # - 4, 16 -> да
# # # - 25, 5 -> да
# # # - 8,9 -> нет

# # # num1 = int(input())
# # # num2 = int(input())

# # # if num1 ** 2 == num2 or num2 ** 2 == num1:
# # #   print('Yes')
# # # else:
# # #   print('No')

# # # 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# # # Примеры:

# # # - 1, 4, 8, 7, 5 -> 8
# # # - 78, 55, 36, 90, 2 -> 90


# # # a = int(input())
# # # b = int(input())
# # # c = int(input())
# # # d = int(input())
# # # e = int(input())

# # # list = [a, b, c, d, e]
# # # max_number = max(list)
# # # print(list)
# # # print(f" Highest valus is", max_number, end='.')
# # # print()

# # max = 0
# #
# # for i in range(5):
# #     i = int(input(f"Enter a number {i + 1}: "))
# #     if num > max:
# #         max = num
# # print(f"Highest value is: {max}.")

# def get_numbers(number):
#     block = []
#     for i in range(number):
#         block.append(int(input('Enter a number: ')))
#     return block


# def find_max(block):
#     max = block[0]
#     for i in block:
#         if i > max:
#             max = i
#     print(max)


# list = get_numbers(5)
# print(find_max(list))

year = int(input())

if 1000 <= year <= 9999:
    if year % 100 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
