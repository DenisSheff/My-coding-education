def encode_string(my_str):
    encoding = ''
    i = 0
    while i < len(my_str):
        el_counter = 1
        while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
            el_counter += 1
            i += 1
        encoding += str(el_counter) + my_str[i]
        i += 1
    return encoding


print(encode_string(input("Enter a value: ")))
