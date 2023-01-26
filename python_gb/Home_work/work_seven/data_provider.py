import logger


def get_user_data():
    user_last_name = input('Enter a last name: ')
    user_name = input('Enter a name: ')
    user_phone_number = input('Enter a phone number: ')
    user_info = input('Enter additional information about a speaker: ')
    print(f'User: {user_name} {user_last_name} is created. \n'
          f'{user_name} {user_last_name} has phone number {user_phone_number}.\n'
          f'Your additional info about the caller is: \n'
          f'{user_info}.')
    logger.log_in(f'User: {user_name} {user_last_name}\n'
                  f'Name: {user_name}\n'
                  f'Last Name: {user_last_name}\n'
                  f'Phone Number: {user_phone_number}\n'
                  f'Information: {user_info}\n'
                  f'--------------------------------------\n')
