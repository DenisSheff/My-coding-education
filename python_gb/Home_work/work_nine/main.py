import os
import pickle
import time

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Update, BotCommand

from filter import IsMoveFilter, LetsPlayFilter, DontPlayFilter
from game_func import check_desk, reset_board, init
from keyboard import create_keyboard, set_main_menu

API_TOKEN: str = '6071356737:AAGXSxqdVJ3qz95qlGWfgVzjrCwTj6EMsOY'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
db: dict = {}
if os.path.exists('db.dat'):
    with open('db.dat', 'rb') as f:
        db = pickle.load(f)


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот!\n'
                         'Я умею играть в крестики-нолики. '
                         '\nСыграем? Да или нет?')
    if message.from_user.id not in db:
        db.setdefault(message.from_user.id, {
            'board': [['\U0001F60E' for _ in range(3)] for _ in range(3)],
            'move': '\U0000274c',
            'count': 0,
            'in_game': False
        })


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Чтобы сыграть введите любое сообщение \n'
                         '[ok, yes, да, ок, сыграем, давай]\n'
                         'либо команду /game.\n'
                         'для выхода из игры команда /cancel.')


@dp.message(LetsPlayFilter())
async def process_help_command(message: Message):
    db[message.from_user.id]["in_game"] = True
    await message.answer(f'Начинаем. Ходит {db[message.from_user.id]["move"]}',
                         reply_markup=create_keyboard(db[message.from_user.id]["board"]))


@dp.message(DontPlayFilter())
async def process_help_command(message: Message):
    time.sleep(1)
    reset_board(db[message.from_user.id]["board"])
    db[message.from_user.id]["in_game"] = False
    db[message.from_user.id]["count"] = 0
    db[message.from_user.id]["move"] = '\U0000274c'
    await message.answer('Жаль \U0001F614. Но если, что зовите - поиграем \U0001F609. ')


@dp.callback_query(IsMoveFilter())
async def button(callback: CallbackQuery):
    if not db[callback.from_user.id]["in_game"]:
        await callback.message.answer('Мы же не играем. Командуй и сыграем \U0001F609.')
        await callback.answer()
    else:
        i = int(callback.data[0])
        j = int(callback.data[1])
        if db[callback.from_user.id]["board"][i][j] == '\U0001F60E':
            db[callback.from_user.id]["board"][i][j] = db[callback.from_user.id]["move"]
            db[callback.from_user.id]["count"] += 1
            if check_desk(db[callback.from_user.id]["board"], db[callback.from_user.id]["move"]):
                time.sleep(1)
                reset_board(db[callback.from_user.id]["board"])
                db[callback.from_user.id]["count"] = 0
                db[callback.from_user.id]["in_game"] = False
                await callback.message.edit_text(f'Ура! Победил {db[callback.from_user.id]["move"]}. Повторим?')
                db[callback.from_user.id]["move"] = '\U0000274c'

            else:
                if db[callback.from_user.id]["count"] < 9:
                    db[callback.from_user.id]["move"] = '\U0000274c' if db[callback.from_user.id][
                                                                            "move"] == '\U00002b55' else '\U00002b55'
                    await callback.message.edit_text(f'Ходит {db[callback.from_user.id]["move"]}',
                                                     reply_markup=create_keyboard(db[callback.from_user.id]["board"]))
                else:
                    time.sleep(1)
                    await callback.message.edit_text('Ничья! Победила дружба). Повторим?')
                    db[callback.from_user.id]["in_game"] = False
                    db[callback.from_user.id]["count"] = 0
                    db[callback.from_user.id]["move"] = '\U0000274c'
                    reset_board(db[callback.from_user.id]["board"])
            await callback.answer()
        else:
            await callback.answer()


@dp.startup()
async def start_bot(bot: Bot):
    print(db)
    await set_main_menu(bot)


@dp.shutdown()
async def stop_bot(bot: Bot):
    with open('db.dat', 'wb+') as f:
        pickle.dump(db, f)
    print('Bot stop.')


if __name__ == '__main__':
    dp.run_polling(bot)