import telebot

bot = telebot.TeleBot('5790395281:AAG1nkwrvqeJWmcvmIjgNNVDIBjHWRB1Wvo')


value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('log', callback_data='log'),
             telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'),)

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'),)

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'),)

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'),)

keyboard.row(telebot.types.InlineKeyboardButton('j', callback_data='j'),
            telebot.types.InlineKeyboardButton('0', callback_data='0'),
            telebot.types.InlineKeyboardButton(',', callback_data='.'),
            telebot.types.InlineKeyboardButton('=', callback_data='='))

@bot.message_handler(commands=['start', 'calculater'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    my_file = open("log.txt", "a")
    my_file.write(data + ' ')
    my_file.close()
    # if data == 'complex':
    #     pass
        
    if data == 'log':
        
        my_file = open("log.txt", "r")
        line_2 = ''
        for line in my_file:
            line_2 += line
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text= line_2, reply_markup=keyboard)
            
        my_file.close()
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
            if len(value) == 1:
                value = ''
    elif data == '=':
        value = str(eval(value))  
        
        my_file = open("log.txt", "a")
        my_file.write(value + '\n')
        my_file.close()
        
    else:
        value += data
    
    if data != "log":
        if (value != old_value and value != '') or ('0' != old_value and value == ''):
            if value == '':
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text= value, reply_markup=keyboard)
                old_value = '0'
       
               
bot.polling()