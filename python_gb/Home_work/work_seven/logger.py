def log_in(text):
    with open('phone_book_data.txt', 'a') as data:
        data.write(text + '\n')


def log_out():
    with open('phone_book_data.txt') as data:
        print(*data.readlines())


def remove_contacts():
    useless_contact = open('phone_book_data.txt', 'r+')
    useless_contact.truncate()
