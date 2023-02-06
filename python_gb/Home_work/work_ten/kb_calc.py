from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_help = KeyboardButton('/help')
btn_rulez = KeyboardButton('/start')


kb_main_menu.add(btn_help, btn_rulez)