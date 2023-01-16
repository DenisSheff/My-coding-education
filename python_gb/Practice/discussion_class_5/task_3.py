# text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'
# new_text = text.lower().replace('абв', '')
# print(new_text)

# def erase_word(elem:str):
#     if 'абв' in elem.lower():
#         elem = elem.replace(text, '')
#     return elem


# text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'
# text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
# print(' '.join(text))


# my_list = 'лдофы фдылабв абв дловфы абвыдфлоф'.split()
#
# st = list(filter(lambda x: 'абв' in x, my_list))
#
# print(my_list)

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')
