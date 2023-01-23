def find_sign(user_list):
    if '*' in user_list or '/' in user_list:
        for i in range(1, len(user_list), 2):
            if user_list[i] == '*':
                result = user_list.pop(i + 1) * user_list.pop(i - 1)
                user_list[i - 1] = result

            elif user_list[i] == '/':
                result = user_list.pop(i + 1) / user_list.pop(i - 1)
                user_list[i - 1] = result

    if '+' in user_list or '-' in user_list:
        for i in range(1, len(user_list), 2):
            if user_list[i] == '+':
                result = user_list.pop(i + 1) + user_list.pop(i - 1)
                user_list[i - 1] = result

            elif user_list[i] == '-':
                result = user_list.pop(i + 1) - user_list.pop(i - 1)
                user_list[i - 1] = result
    return user_list


user_expression = '3*(10+12)'
# user_list = [i for i in user_expression]
# print(user_list)
# for i, el in enumerate(user_expression):
#     if not el.isdigit():
# print(eval(user_expression))
user_number = ''
new_user_list = []

for i, el in enumerate(user_expression):
    if el.isdigit():
        user_number += el
    elif el in '()':
        new_user_list.append(el)
    else:
        new_user_list.append(int(user_number))
        new_user_list.append(el)
        user_number = ''
if user_expression[-1] == ')':
    new_user_list.insert(-1, int(user_number))
else:
    new_user_list.append(int(user_number))

if '(' in new_user_list:
    index_one = new_user_list.index('(')
    index_two = new_user_list.index(')')
    new_user_list = new_user_list[:index_one] + find_sign(new_user_list[index_one + 1:index_two]) + new_user_list[index_two + 1:]
new_user_list = find_sign(new_user_list)
print(*new_user_list)
