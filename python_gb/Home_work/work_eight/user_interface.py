import logger


def user_choose():
    menu = input("Menu:\n"
                 "1. Add a new employee.\n"
                 "2. Show all information about the organisation.\n"
                 "3. Change employee's information.\n"
                 "4. Remove an employee.\n"
                 "Press 'Return' button to finish work of the application.\n"
                 "Choose an option: ")
    logger.log_in('User chose an option: ' + menu + ';')
    return
