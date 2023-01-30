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
    student_data = [last_name, name, patronymic_name, birth_date,phone_number, address, class_name]
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
    pass


def edit_student():
    pass


def edit_class():
    pass


def remove_info():
    student_id = int(input("Enter student's id: "))
    global all_classes
    global all_students
    all_classes[all_students[student_id][- 1]].remove(student_id)
    del all_students[student_id]
