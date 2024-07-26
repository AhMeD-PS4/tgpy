from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, Updater, MessageHandler, filters
from telegram.constants import ParseMode



async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mentioning = update.effective_sender.mention_markdown_v2();
    await context.bot.send_message(chat_id=update.effective_chat.id,
                parse_mode=ParseMode.MARKDOWN_V2,
                text=f"I'm a bot, please talk to me\!  {mentioning}",
                );

