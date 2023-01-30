import export_data
from import_data import *
import logger


def choose_option():
    user_choice = input('Welcome! This is a school book. You can find here all the information you need. '
                        'Choose one of the options to continue:\n'
                        '1. Add info\n'
                        '2. Edit info\n'
                        '3. Remove student\n'
                        '4. Print all information to console\n'
                        '5. Export the information\n'
                        'Exit\n'
                        'Your choice: ')
    if user_choice == '1':
        add_choice = input('Choose an option: \n'
                           '1. Add a student\n'
                           '2. Add a class')
        if add_choice == '1':
            create_student()
        elif add_choice == '2':
            create_class()
    elif user_choice == '2':
        edit_choice = input('Choose an option: \n'
                            '1. Change information about a student\n'
                            '2. Change class for a student')
        if edit_choice == '1':
            edit_student()
        elif edit_choice == '2':
            edit_class()
    elif user_choice == '3':
        remove_info()
    elif user_choice == '4':
        to_console()
    elif user_choice == '5':
        to_csv()
    elif user_choice == 'Exit'.lower():
        return
    else:
        print('Error! Pay attention: you need to choose one of the options in the menu above.\n'
              'Try one more time.')
        choose_option()

