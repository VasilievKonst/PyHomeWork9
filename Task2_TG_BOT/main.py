from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from command import *

app = ApplicationBuilder().token("6168931532:AAFaHK_O3dhcflS05EJCXLF2q3AbS2TzFXg").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("mult", mult_command))


print('server start')

app.run_polling()