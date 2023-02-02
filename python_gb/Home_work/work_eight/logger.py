def log_in(data):
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write(data + '\n')
