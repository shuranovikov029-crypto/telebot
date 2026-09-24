import telebot
from telebot import types
token = "8299256642:AAEVaGQQ7ILUWf-ofzz5EdRra2CDJhkQgkQ"
bot = telebot.TeleBot(token)
@bot.message_handler(cmd= ("start"))
def start(message):
    клава = types.InlineKeyboardMarkup()
    клава.add(types.InlineKeyboardButton,"ссылка кнопка", url = "https//ru.wikipedia.org")
    bot.reply_to(message,"это сайт википедии на нем можно узнать оооочень многое",reply_markup=клава)
    print("бот запущен...") 
    bot.infinity_polling()