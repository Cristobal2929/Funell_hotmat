from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Tu token de BotFather
TOKEN = '8117601252:AAGexqWVtfYaSurSe91zW0IUj3H1LKRx5KI'

# Mensaje de bienvenida con botones
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📺 Ver entrenamiento", url="https://go.hotmart.com/cr_2w9C0Gbpdmg9FX312kdTyk9mivL")],
        [InlineKeyboardButton("❓ Tengo dudas", callback_data='dudas')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "¡Hola! 👋 Bienvenido/a al sistema que está cambiando vidas.\n\n"
        "¿Qué te gustaría hacer ahora?", reply_markup=reply_markup
    )

# Respuestas automáticas según texto
def responder(update, context):
    texto = update.message.text.lower()

    if "precio" in texto:
        update.message.reply_text("💸 El entrenamiento comienza GRATIS. No hay riesgo, solo aprendizaje.")
    elif "hola" in texto or "buenas" in texto:
        update.message.reply_text("¡Hola! ¿Quieres ver el entrenamiento gratuito o tienes dudas?")
    elif "duda" in texto or "ayuda" in texto:
        update.message.reply_text("¡Dime tu duda y te responderé enseguida!")
    else:
        update.message.reply_text("Gracias por escribirme 🙌. Revisa el entrenamiento aquí 👉 https://go.hotmart.com/cr_2w9C0Gbpdmg9FX312kdTyk9mivL")

# Acciones al pulsar botones (callback)
def botones(update, context):
    query = update.callback_query
    query.answer()
    if query.data == "dudas":
        query.edit_message_text(text="❓ Puedes escribirme tu duda y te responderé enseguida.")

# Ejecutar bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, responder))
    dp.add_handler(MessageHandler(Filters.command, responder))
    dp.add_handler(MessageHandler(Filters.all, responder))
    dp.add_handler(CallbackQueryHandler(botones))

    updater.start_polling()
    print("✅ Bot activo... esperando mensajes.")
    updater.idle()

if __name__ == '__main__':
    main()
