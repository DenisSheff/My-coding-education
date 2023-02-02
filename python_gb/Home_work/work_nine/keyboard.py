from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand


def create_keyboard(board: list) -> InlineKeyboardMarkup:
    b1 = InlineKeyboardButton(text=f'{board[0][0]}', callback_data=f'00')
    b2 = InlineKeyboardButton(text=f'{board[0][1]}', callback_data=f'01')
    b3 = InlineKeyboardButton(text=f'{board[0][2]}', callback_data=f'02')
    b4 = InlineKeyboardButton(text=f'{board[1][0]}', callback_data=f'10')
    b5 = InlineKeyboardButton(text=f'{board[1][1]}', callback_data=f'11')
    b6 = InlineKeyboardButton(text=f'{board[1][2]}', callback_data=f'12')
    b7 = InlineKeyboardButton(text=f'{board[2][0]}', callback_data=f'20')
    b8 = InlineKeyboardButton(text=f'{board[2][1]}', callback_data=f'21')
    b9 = InlineKeyboardButton(text=f'{board[2][2]}', callback_data=f'22')

    return InlineKeyboardMarkup(inline_keyboard=[
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
    ])


async def set_main_menu(bot: Bot):
    # Создаем список с командами для кнопки menu
    print('Bot working...')
    main_menu_commands = [
        BotCommand(command='/start', description='Начать работу боту'),
        BotCommand(command='/help', description='Справка по работе бота'),
        BotCommand(command='/game', description='Сыграть в крестики-нолики'),
        BotCommand(command='/cancel', description='Сбросить игру'),
    ]
    await bot.set_my_commands(main_menu_commands)