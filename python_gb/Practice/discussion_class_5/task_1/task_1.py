# Reading the file
# f = open('/Users/denisshevchenko/Desktop/My-coding-education/python_gb/Practice/discussion_class_5/task_1/file.txt', 'r')
# data = f.read().split()
# f.close()
#
# # Make Integer value, using map()
# data = list(map(int, data))
# print(data)
# for i, el in enumerate(data[:-1]):
#     if el != data[i + 1] - 1:
#         print(data[i + 1] - 1)

# with open('/Users/denisshevchenko/Desktop/My-coding-education/python_gb/Practice/discussion_class_5/task_1/file.txt', 'r') as data:
#     nums_list = [int(el) for el in data.read().split()]
#     counter = nums_list[0] + 1
# print(nums_list)
# for index in range(1, len(nums_list)):
#     if counter != nums_list[index]:
#         print(counter)
#         break
#     else:
#         counter += 1
n = [1, 2, 3, 4, 5, 6, 7, 9]
print(*[val for i, val in enumerate(n[1:]) if val != n[i] + 1])
