def log_in(date):
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write(date + '\n')


def log_out():
    with open('log.txt') as data:
        print(*data.readlines())
