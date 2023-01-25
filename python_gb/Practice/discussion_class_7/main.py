from calc import calculate_expression
from user_interface import get_data
import logger
import controller


# first_value, second_value, math_operator = get_data()
# logger.log_res(calculate_expression(logger.log_in(fir
# st_value, second_value, math_operator)))
# print(calculate_expression(first_value, second_value, math_operator))
user_input = input('Calculation – 1\n'
                   'Logging out – 2.\n'
                   'Option: ')
if user_input == '1':
    print(controller.control_data())
else:
    logger.log_out()
