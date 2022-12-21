# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Enter a value: "))


def find_f(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * find_f(number - 1)


my_list = []
for i in range(1, n + 1):
    my_list.append(find_f(i))

print(f"Multiplication of numbers from 1 to {n} is {my_list}.")
