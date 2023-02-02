from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message


class IsMoveFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        try:
            moves = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
            return callback.data in moves
        except:
            return False


class LetsPlayFilter(BaseFilter):
    async def __call__(self, message: Message):
        try:
            approval = ['/game', 'ok', 'yes', 'да', 'ок', 'сыграем', 'давай', 'game', 'игра']
            return message.text.lower() in approval
        except:
            return False


class DontPlayFilter(BaseFilter):

    async def __call__(self, message: Message):
        try:
            reject = ['/cancel', 'no', 'not', 'нет', 'не хочу', 'потом', 'не']
            if message.text.lower() in reject:
                return True
        except:
            return False