import telebot
import time
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands =["start"])
def send_velcome(message);
   global chat_id
   bot.reply_to(message, "Привет. Я твой бот-помощник")

