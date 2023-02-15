from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from log_create import *

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!\nLet`s start!\n/sum\n/sub\n/div\n/mult\n')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split() 
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split() 
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split() 
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split() 
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')
