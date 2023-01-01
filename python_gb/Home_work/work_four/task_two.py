# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


number = int(input("Enter a number: "))
simple_number = 2  
my_list = []
recent_number = number

while simple_number <= number:
    if number % simple_number == 0:
        my_list.append(simple_number)
        number //= simple_number
        simple_number = 2
    else:
        simple_number += 1
print(f"Order of simple multiple numbers of number {recent_number} is listed here: {my_list}.")