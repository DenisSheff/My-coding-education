from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

base = 2021
player = 1

async def g_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player
    global base
    if base > 0:
        await update.message.reply_text(f'На столе {base} конфет.')
        await update.message.reply_text(f'Игрок {player} введите количество конфет сколько Вы возьмете: ')
        text = update.message.text.split()
        text = int(text[1])
        base -= text
        if base <= 0:
            await update.message.reply_text(f'На столе не осталось конфет, вы выиграли!.')
        else:
            await update.message.reply_text(f'На столе отсалось {base} конфет.')
            player = 3-player
    else:
        await update.message.reply_text('Конфеты кончились, отстань.')