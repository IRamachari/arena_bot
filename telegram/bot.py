import os
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.commands import start

def run_bot():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
