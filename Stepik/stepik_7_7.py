
# MODULE 7.8

# number = int(input())
# for i in range(number):
#     for j in range(3):
#         print(number, end=' ')
#     print()

# number = int(input())
# for i in range(number):
#     for _ in range(5):
#         print(i + 1, end=' ')
#     print()

# number = int(input())
# for i in range(1, number + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# number = int(input())
# center = number // 2 + 1
# count = 0
# for i in range(1, number + 1):
#     if i > center:
#         count -= 1
#     else:
#         count += 1
#     for j in range(count):
#         print('*', end='')
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     print(str(i) * i)
#
# number = int(input())
# for i in range(1, number + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# 28n+30k+31m=365
# 13 12 11
# total = 0
# for n in range(1, 11):
#     for k in range(1, 6):
#         for m in range(1, 2001):
#             if 10 * n + 5 * k + 0.5 * m == 100:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m,)
# print('Общее количество натуральных решений =', total)

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a, b, c, d, e)
#                         print(a + b + c + d + e)
#                         break
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(sum ** (1/5))
#                 if sum == e ** 5:
#                     print(a, b, c, d, e)
#                     print(a + b + c + d + e)
#                     break

# total = 0
# for i in range(1, int(input()) + 1):
#     for j in range(i):
#         total += 1
#         print(total, end=' ')
#     print()

# for i in range(1, int(input()) + 1):
#     for j in range(i):
#         print(j + 1, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()
