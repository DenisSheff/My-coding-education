from calc import calculate_expression
from user_interface import get_data
import logger


def control_data():
    first_value, second_value, math_operator = get_data()
    result = calculate_expression(first_value, second_value, math_operator)
    return result
