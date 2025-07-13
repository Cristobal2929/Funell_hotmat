import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Cargar variables de entorno desde .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Error: No se encontró el token de Telegram en .env")
    exit(1)

def start(update: Update, context: CallbackContext):
    mensaje = (
        "¡Hola!\n\n"
        "Te invito a visitar la página para descargar la guía Mentalidad del Éxito:\n"
        "https://http://127.0.0.1:5000/\n\n"
        "¡Mucho éxito! 🚀"
    )
    update.message.reply_text(mensaje)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("Bot arrancando...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
