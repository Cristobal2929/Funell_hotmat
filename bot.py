from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
FUNNEL_LINK = 'https://tudominio.com'  # Cambia por el URL donde esté tu funnel

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"¡Hola! Te invito a descargar un ebook gratuito que te ayudará a [beneficio]. Aquí el link: {FUNNEL_LINK}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
