# num1 = 4
# num2 = 6
# num1 += num2
# num1 *= num1
# print(num1)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a = int(input())
# b = int(input())
# count = 0
# for i in range(a, b + 1):
#     if i % 10 == 4 or i % 10 == 9:
#         count += 1
# print(count)

# number = int(input())
# count = 0
# for i in range(number):
#         count += int(input())
# print(count)

from math import *
#
# num = int(input())
# count = 0
# for i in range(1, num + 1):
#     count += (1 / i)
# print(count - log(num))

# number = int(input())
# total = 0
# for i in range(1, number + 1):
#     if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
#         total += i
# print(total)

# number = int(input())
# counter = 1
# for i in range(1, number + 1):
#     counter *= i
# print(counter)

# count = 1
# for i in range(1, 10 + 1):
#     number = int(input())
#     if number > 0:
#         count = number * count
# print(count)

# number = int(input())
# total = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         total += i
# print

# number = int(input())
# total = 0
# for i in range(1, number +1):
#     if i % 2 == 0:
#         total -= i
#     if i % 2 != 0:
#         total += i
# print(total)

# n = int(input())
# max1 = max2 = 1         # пусть самое большое число это минимально возможное
# for i in range(1, n+1): # цикл от 1 до n
#     a = int(input())    # получаем следующее число
#     if a > max1:        # если введенное число больше нашего максимума, то это новый максимум
#         max2 = max1     # запоминаем предыдущее наибольшее число в переменной max2
#         max1 = a        # а само это число на входе становится наибольшим
#     elif a > max2:      # если число не больше max1, то проверяем больше ли оно второго max2
#         max2 = a
# print(max1)
# print(max2)

# even = True
# for i in range(1, 10 + 1):
#     number = int(input())
#     if number % 2 != 0:
#         even = False
# if even:
#     print('Yes')
# else:
#     print('No')
