from logger import log_in


all_classes = {}
all_students = {}
id_student = 1


def create_student():
    last_name = input("Enter student's last name: ")
    name = input("Enter student's name: ")
    patronymic_name = input("Enter student's patronymic name: ")
    birth_date = input("Enter student's date of birth: ")
    phone_number = input("Enter student's phone number: ")
    address = input("Enter student's address: ")
    class_name = input("Enter student's form and letter: ")
    log_in(f'Student: {last_name} {name} {patronymic_name}\n'
           f'Birthday Date: {birth_date}\n'
           f'Phone number: {phone_number}\n'
           f'Home Address: {address}\n'
           f'Form: {class_name}\n'
           f'--------------------------\n')
    student_data = [last_name, name, patronymic_name, birth_date, phone_number, address, class_name]
    global all_students
    global id_student
    if class_name not in all_classes:
        create_class(class_name)
    all_classes[class_name].append(id_student)
    all_students[id_student] = student_data
    id_student += 1


def create_class(name_class=False):
    if not name_class:
        name_class = input('Enter class number: ')
    all_classes[name_class] = []


def change_class():
    global all_classes
    global all_students
    student_id = int(input("Enter student's id: "))
    old_class_number = all_students[student_id][-1]
    new_class_number = input('Enter a new class for the student: ')
    all_classes[old_class_number].remove(student_id)
    all_classes[new_class_number].append(student_id)


def edit_student():
    global all_classes
    global all_students
    student_id = int(input("Enter student's id that is needed to be edited: "))
    new_last_name = input("Enter student's edited last name: ")
    new_name = input("Enter student's edited name: ")
    new_patronymic_name = input("Enter student's edited patronymic name: ")
    new_birth_date = input("Enter student's edited date of birth: ")
    new_phone_number = input("Enter student's edited phone number: ")
    new_address = input("Enter student's edited address: ")
    class_name = all_students[[student_id][-1]]
    new_student_data = [new_last_name, new_name, new_patronymic_name,
                        new_birth_date, new_phone_number, new_address, class_name]
    all_students[student_id] = new_student_data


def remove_info():
    student_id = int(input("Enter student's id: "))
    global all_classes
    global all_students
    all_classes[all_students[student_id][- 1]].remove(student_id)
    del all_students[student_id]



