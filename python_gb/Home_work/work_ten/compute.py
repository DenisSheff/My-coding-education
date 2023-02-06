import view

def calculate_expression(first_value, second_value, math_operator):
    logger.log_all(f'Settling the account: {first_value} {math_operator} {second_value}.\n')
    if math_operator == '+':
        return first_value + second_value
    elif math_operator == '-':
        return first_value - second_value
    elif math_operator == '*':
        return first_value * second_value
    elif math_operator == '/':
        return first_value / second_value