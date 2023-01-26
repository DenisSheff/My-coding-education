import data_provider
import logger


print('Phone book')


def make_user_choice():
    user_choice = input('You may: \n'
                        '1: create a new user.\n'
                        '2: show all the data.\n'
                        '3: remove all contacts\n'
                        'Choose an option: ')
    if user_choice == '1':
        data_provider.get_user_data()
        extra_contact = input('Would you like to add one more contact? Yes or no: ')
        if extra_contact == 'Yes'.lower():
            data_provider.get_user_data()
        else:
            print('Adding a contact is declined.')
    elif user_choice == '2':
        logger.log_out()
    elif user_choice == '3':
        logger.remove_contacts()
    else:
        print('You need to choose one of the options to continue: ')
        make_user_choice()

