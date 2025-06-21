import os
import telegram
from telegram.ext import Updater, CommandHandler

# Ambil token dari environment variable
TOKEN = os.environ.get("BOT_TOKEN")

# Inisialisasi objek bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Command /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Bot kamu sudah aktif di Railway.")

# Daftarkan command ke dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Jalankan bot
updater.start_polling()
updater.idle()
