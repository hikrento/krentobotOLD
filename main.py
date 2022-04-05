import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

yes_message = 'CAACAgIAAxkBAAEEYIViTCKiFQkhhgPXwrTzFIK38XaJKgACLhcAAnbsqUhSONZmcbrzYSME'
no_message = 'CAACAgIAAxkBAAEEYIZiTCKjxLbzkPY0i_2PZxnFcaKr3AACVRYAApObqUglci59k4GQTiME'

@bot.message_handler(commands=['start'])
def welcome(message):
    #buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    randButton = types.KeyboardButton('Fortune teller')
    invButton = types.KeyboardButton('Invite me to orden!')
 
    markup.add(randButton, invButton)
    
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYINiTCDoqptpW2jIbdJhcSbJuOQ_PAACcBYAAjfNqUhB9xKWT5sU8yME')
    bot.send_message(message.chat.id, "Приветик, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Fortune teller':
            rnd = random.randint(0,1)
            if (rnd == 0):
                bot.send_sticker(message.chat.id, yes_message)
            else:
                bot.send_sticker(message.chat.id, no_message)
        elif message.text == 'Invite me to orden!':
            bot.send_message(message.chat.id, 'Send me <b>password</b> to unlock link access', parse_mode='html')
        elif message.text == '49':
            bot.send_message(message.chat.id,'t.me/+ygdHL1GTWZllMTYy')
        else:
            bot.send_message(message.chat.id, 'I dont understand what do u want!!!')
    

# RUN
bot.polling(none_stop=True)