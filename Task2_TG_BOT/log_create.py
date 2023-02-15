from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

def log (update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('data.csv', 'a')
    f.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.datetime.now()}\n')
    f.close()
