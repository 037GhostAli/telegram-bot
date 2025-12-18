import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ✅ توکن از Environment Variable گرفته میشه، دیگه تو کد نیست
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    webapp = WebAppInfo(
        url="https://037ghostali.github.io/Free"
    )

    button = InlineKeyboardButton(
        text="🎁 ادامه و ورود به طرح ویژه",
        web_app=webapp
    )

    markup.add(button)

    bot.send_message(
        message.chat.id,
        "🎉 به ربات اینترنت رایگان یکساله خوش آمدید!\n\n"
        "برای ادامه روی دکمه زیر کلیک کنید 👇",
        reply_markup=markup
    )

bot.polling()
