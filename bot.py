from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# Get bot token from environment variable
TOKEN = os.getenv("TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Send Money", callback_data="send_money")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to Auto Payment Bot!", reply_markup=reply_markup)

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "send_money":
        payment_link = "bkash://payment?to=01884682406&amount=500"
        query.message.reply_text(f"Click here to send money:\n[Pay Now]({payment_link})", parse_mode="Markdown")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_click))  # ✅ CallbackQueryHandler যুক্ত করা হয়েছে

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
