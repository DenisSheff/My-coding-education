def write_data(date):
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write(date + '\n')
