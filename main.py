import telebot
import webbrowser

bot = telebot.TeleBot('TOKEN_BOT') 

@bot.message_handler(commands=['site']) #to make this one work when you need to import webbrowser
def site(message):
    webbrowser.open('https//')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name} {message.from_user.last_name}') #info User

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}') #reply_to() - sends messages

bot.polling(none_stop=True)