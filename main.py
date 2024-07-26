################# IMPORTING #################
import os
from dotenv import load_dotenv
load_dotenv();
BOT_TOKEN = os.getenv("BOT_TOKEN")


import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, Updater, MessageHandler, filters
from telegram.constants import ParseMode
from start import start1
from handling import echo




################# CODE #################

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
);

################# RUNNING THE BOT #################

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start1(update, context);

async def echo1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await echo(update, context);

def main():
    application = ApplicationBuilder().token(f'{BOT_TOKEN}').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo1)
    start_handler = CommandHandler(['start','hi'], start)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling();


if __name__ == '__main__':
    main();