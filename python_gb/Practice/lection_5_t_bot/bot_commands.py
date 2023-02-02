from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'Hi, {update.effective_user.first_name}')


def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'/hi\n/time\n/help')


# def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hi, {update.effective_user.first_name}')
