from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("6139892299:AAFbENaXvxQgHLuyQbp9-3JbNhhxoRWFob4").build()
print('Hi')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
