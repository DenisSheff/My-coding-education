from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#
#
# async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     a = update.message.text[1:]
#     await update.message.reply_text(f'{" ".join(list(i for i in a.split() if "абв" not in i))}')
async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while True:
        update.message.reply_text()

app = ApplicationBuilder().token("5920982726:AAFzgveKIBL_BrBtc3Usapw26H6uDWYPDZU").build()
print('Server is activated.')


app.add_handler(CommandHandler("g_1", bot_commands.g_1))
# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("remove", remove))

app.run_polling()


