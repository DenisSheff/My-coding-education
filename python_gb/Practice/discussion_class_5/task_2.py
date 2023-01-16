

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
print(my_list)
new_list = list()
new_list.append(my_list[0])

for i, el in enumerate(my_list):
    if el > new_list[-1]:
        new_list.append(el)
print(new_list)

