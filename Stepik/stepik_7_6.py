# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# Наименьший делитель
# На вход программе подается число n > 1.
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.

# number = int(input())
# for i in range(2, number + 1):
#     if number % i == 0:
#         print(i)
#         break

# Следуй правилам
# На вход программе подается натуральное число n.
# Напишите программу, которая выводит числа от 1 до n включительно за исключением:
#
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.

# number = int(input())
# for i in range(1, number + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37  or 78 <= i <= 87:
#         continue
#     print(i)

# n = int(input())
# for i in range(1, n + 1):
#     if i in range(5, 10):
#         continue
#     if i in range(17, 38):
#         continue
#     if i in range(78, 88):
#         continue
#     print(i)

# for i in range(1, int(input()) + 1):
#     if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
#         continue
#     print(i)

