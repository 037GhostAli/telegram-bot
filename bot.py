import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
import threading
import requests
import time

# گرفتن توکن از Environment Variable
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# پیام خوش آمد
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    webapp = WebAppInfo(url="https://037ghostali.github.io/Free")
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

# -------------------------
# Flask server ساده برای Render
# -------------------------
app = Flask(__name__)
@app.route("/")
def index():
    return "Bot is running!"

# اجرای ربات در Thread جدا
threading.Thread(target=bot.polling, daemon=True).start()

# Self ping برای جلوگیری از Timeout Render
def keep_alive():
    while True:
        try:
            requests.get("http://localhost:" + os.environ.get("PORT", "10000"))
        except:
            pass
        time.sleep(300)  # هر ۵ دقیقه ping

threading.Thread(target=keep_alive, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
