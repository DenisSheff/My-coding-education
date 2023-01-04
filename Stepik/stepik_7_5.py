# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# number = int(input())
new_number =[]
# while number != 0:
#     last_digit = number % 10
#     last_digit_first = last_digit
#     number //= 10
#     print(last_digit_first)

# number = int(input())
# new_number = []
# while number != 0:
#     last_digit = number % 10
#     new_number.append(last_digit)
#     number //= 10
# print(*new_number, sep='')

# number = int(input())
# new_number = []
# while number != 0:
#     last_digit = number % 10
#     new_number.append(last_digit)
#     number //= 10
# print(f"Максимальная цифра равна {max(new_number)}")
# print(f'Минимальная цифра равна {min(new_number)}')
from math import pow


# number = int(input())
# old_number = number
# sum_counter = 0
# digits_counter = 0
# multiplication_counter = 1
# while number != 0:
#     last_digit = number % 10
#     number //= 10
#     sum_counter += last_digit
#     digits_counter += 1
#     multiplication_counter *= last_digit
# print(sum_counter)
# print(digits_counter)
# print(multiplication_counter)
# print(sum_counter / digits_counter)
# print(old_number // 10 ** (digits_counter - 1))
# print((old_number // 10 ** (digits_counter - 1)) + old_number % 10)

# number = int(input())
# second_digit = 0
# while number > 9:
#     second_digit = number % 10
#     number //= 10
# print(second_digit)

# number = int(input())
# flag = True
# while number >= 10:
#     last_digit = number % 10
#     next_to_last_digit = number % 100 // 10
#     if last_digit > next_to_last_digit:
#         flag = False
#         break
# if flag:
#     print("YES")
# else:
#     print("NO")
