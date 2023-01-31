def log_in(date):
    with open('employees.txt', 'a', encoding='utf=8') as file:
        file.write(date + '\n')


def log_out():
    with open('employees.txt') as data:
        print(*data.readlines())
