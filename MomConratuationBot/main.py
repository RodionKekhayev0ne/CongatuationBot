import telebot

bot = telebot.TeleBot("7020522689:AAFNm222xRwgaLocCSNc5GJVcPvzosTTDME")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Working")
bot.infinity_polling()