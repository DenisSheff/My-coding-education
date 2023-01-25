# def log_in(value_one, value_two, math_operator):
#     with open('logging.txt', 'a') as data:
#         data.write(f'{value_one}, {math_operator}, {value_two}\n')
#         return value_one, math_operator, value_two
#
#
# def log_res(result):
#     with open('logging.txt', 'a') as data:
#         data.write(f'{result}\n')
#         return result
def log_all(text):
    with open('log.txt', 'a') as data:
        data.write(text + "\n")


def log_out():
    with open('log.txt') as data:
        print(data.readlines())
