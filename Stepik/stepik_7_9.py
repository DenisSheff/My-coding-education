# number_a = int(input())
# number_b = int(input())
# total_sum = 0
# max_total = 0
# num_x = 0
# for i in range(number_a, number_b + 1):
#     for k in range(1, i + 1):
#         if i % k == 0:
#             total_sum += k
#     if total_sum >= max_total:
#         max_total = total_sum
#         num_x = i
#     total_sum = 0
# print(num_x, max_total)


# number = int(input())
# count = 0
# for i in range(1, number + 1):
#     for k in range(1, i + 1):
#         if i % k == 0:
#             count += 1
#     print(str(i) + '+' * count)
#     count = 0

# 192 = 1 + 9 + 2 = 12 = 1 + 2 = 3

# number = int(input())
# while number > 9:
#     sum = 0
#     while number != 0:
#         sum += number % 10
#         number //= 10
#     number = sum
# print(number)

# number = int(input())
# factorial_s = 1
# while number > 1:
#     factorial_s *= number
#     number -= 1
# print(factorial_s)
#
# number_f = int(input())
# f_sum = 1
# if number_f == 0:
#     f_sum = 1
# if number_f > 0:
#     f_sum = number_f * (number_f - 1)
# print(f_sum)
#
# from math import factorial
#
# number_f_2 = int(input())
# sum_f = 0
# for _ in range(1, number_f_2):
#     sum_f += factorial(number_f_2)
# print(sum_f)

# my_num = int(input())
# factorial_num = 1
# sum_f = 0
# for i in range(1, my_num + 1):
#     for k in range(1, i + 1):
#         factorial_num *= k
#     sum_f += factorial_num
#     factorial_num = 1
# print(sum_f)

# number_a = int(input())
# number_b = int(input())
# counter = 0
# for i in range(number_a, number_b + 1):
#     for k in range(1, i + 1):
#         if i % k == 0:
#             counter += 1
#     if counter == 2:
#         print(i)
#     counter = 0

# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)
#
# number = int(input())
# for i in range(1, number + 1):
#     if i == 1 or i == number:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')

# num = int(input())
# while num >= 1000:
#         num //= 10
# print(num % 10)

# num = int(input())
# three_sum = 0
# last_digit_counter = 0
# last_digit = num % 10
# even_counter = 0
# sum_above_five = 0
# p7 = 1
# counter5 = 0
# while num != 0:
#     if num % 10 == 3:
#         three_sum += 1
#     if last_digit == num % 10:
#         last_digit_counter += 1
#     if num % 10 % 2 == 0:
#         even_counter += 1
#     if num % 10 > 5:
#         sum_above_five += num % 10
#     if num % 10 > 7:
#         p7 *= num % 10
#     if num % 10 == 0 or num % 10 == 5:
#         counter5 += 1
#     num //= 10
# print(three_sum)
# print(last_digit_counter)
# print(even_counter)
# print(sum_above_five)
# print(p7)
# print(counter5)

# text = input()
# new_text = int(text)
# new_sum = 0
# while new_text > 0:
#     last_digit = new_text % 10
#     new_sum += last_digit
#     new_text //= 10
# print(new_sum)

# text = input()
# count = 0
# for i in range(0, 10):
#     if str(i) in text:
#         count += 1
# if count >= 1:
#     print('Цифра')
# else:
#     print('Цифр нет')


# text = input()
# print(f'Символ + встречается {text.count("+")} раз')
# print(f'Символ * встречается {text.count("*")} раз')

# text = input()
# counter = 0
# for i in range(0, len(text)):
#     if text[i] == text[i - 1]:
#         counter += 1
# print(counter)

# text = input()
# odds_counter = 0
# even_counter = 0
# for i in range(0, len(text)):
#     if text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         odds_counter += 1
#     elif text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         even_counter += 1
# print(f'Количество гласных букв равно {even_counter}')
# print(f'Количество согласных букв равно {odds_counter}')


# def cut_list(my_list):
#     if len(my_list) % 2 != 0:
#         new_list = my_list[len(my_list) // 2 + 1:]
#         new_list2 = my_list[:len(my_list) // 2 + 1]
#     else:
#         new_list = my_list[len(my_list) // 2:]
#         new_list2 = my_list[:len(my_list) // 2]
#     return new_list + new_list2
#
#
# text = input()
# print(cut_list(text))
#
# s = 'i Learn Python language'
# print(s.capitalize())
#
#
# s = 'i LEARN Python LAnguaGE'
# print(s.lower())
#
# s1 = 'a'
# s2 = s1.upper()
# print(s1, s2)
#
# s = 'i LEARN Python LAnguaGE'
# print(s.upper())
#
# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# text = input()
# if text == text.title():
#     print('YES')
# else:
#     print('NO')

# text = input().lower()
# if 'хорош' in text:
#     print('YES')
# else:
#     print('NO')

# text = input()
# text2 = text.upper()
# counter = 0
# for i in range(len(text)):
#     if text[i] != text2[i]:
#         counter += 1
# print(counter)
