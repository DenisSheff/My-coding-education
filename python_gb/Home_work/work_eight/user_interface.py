import logger
import controller


def show_menu():
    user_choice = input("Menu:\n"
                        "1. Add a new employee.\n"
                        "2. Show all information about the organisation.\n"
                        "3. Change employee's information.\n"
                        "4. Remove an employee.\n"
                        "Press 'Return' button to finish work of the application.\n"
                        "Choose an option: ")
    if user_choice == '1':
        controller.add_employee()
    elif user_choice == '2':
        logger.log_out()
    elif user_choice == '3':
        info_edit = input("What do you need to edit?\n"
                          "1. Employee's information.\n"
                          "2. Employee's division.")
        if info_edit == '1':
            controller.edit_employee()
        elif info_edit == '2':
            controller.edit_division()
    elif user_choice == '4':
        controller.remove_employee()
    else:
        print('Work of the application is over.')
