import user_input

def view_data(data, title):
    title = (f'{user_input.num_1} {user_input.oper} {user_input.num_2}')
    print(f'{title} = {data}')

def get_value():
    return user_input.inp2()