import logger


def add_employee():
    employee_name = input('Enter a name: ')
    employee_last_name = input('Enter a last name: ')
    employee_phone_number = input('Enter a phone number: ')
    employee_info = input('Enter additional information: ')
    print(f'User: {employee_name} {employee_last_name} is created. \n'
          f'{employee_name} {employee_last_name} has phone number {employee_phone_number}.\n'
          f'Your additional info about the caller is: \n'
          f'{employee_info}.')
    logger.log_in(f'Employee: {employee_name} {employee_last_name}\n'
                  f'Name: {employee_name}\n'
                  f'Last Name: {employee_last_name}\n'
                  f'Phone Number: {employee_phone_number}\n'
                  f'Information: {employee_info}\n'
                  f'--------------------------------------\n')
    print('Employee was added to the list.')


def edit_employee():
    pass


def edit_division():
    pass


def remove_employee():
    pass
