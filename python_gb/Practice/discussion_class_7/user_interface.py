import logger


def get_data():
    value_x = input('Enter a number: ')
    value_y = input('Enter a number: ')
    user_operator = input('Enter an operator for expression: ')

    logger.log_all(f'We receive numbers {value_x}, operator = "{user_operator}" and {value_y}.')

    if 'j' in value_x:
        value_x = complex(value_x)
    else:
        value_x = int(value_x)

    if 'j' in value_y:
        value_y = complex(value_y)
    else:
        value_y = int(value_y)

    return value_x, value_y, user_operator


def set_data():
    pass


# def check_data(data):
#     data = get_data()
#     if 'j' in data:
#         a, b = complex(data)
#     else:
#         a, b = int(data)
#     return a, b

