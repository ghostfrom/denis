# -*- coding: utf-8 -*-

import telebot
from telebot import types
import random
from time import time
import urllib.request as urllib2
otmazki = ['ТЫ ПИДОР','НАХУЙ ПАРЫ','Я БУХАТЬ. КТО СО МНОЙ?','ШО?','Отстань', 'Вызываю Антонюка']
otmazki1 = ['В АРМИИ','ПРЫГАЙ В ОКНО','Здравствуй небо в облаках, здравствуй юность в сапогах...','Give me your money','Та зачем оно тебе нужно?', 'Вызываю Антонюка']
otmazki3 = ['ИДИ НАХУЙ', 'Вызываю Антонюка']
random_message = lambda: random.choice(otmazki)
random_message1 = lambda: random.choice(otmazki1)
random_message3 = lambda: random.choice(otmazki3)

bot = telebot.TeleBot("549489621:AAHjOvAtZMo-eOvedtl4roEzyXCDHla4h54")
 

 
GROUP_ID = -1001285627060 

strings = {
    "ru": {
        "ro_msg": "Этому ,кхм-кхм,'пользователю', запрещено общаться в течении 5 минут."
    },
    "en": {
        "ro_msg": "Этому ,кхм-кхм,'пользователю', запрещено общаться в течении 5 минут."
    }
}

def get_language(lang_code):
   
    if lang_code == "ru":
        return "ru"

restricted_messages = ('ЦЫЦ', 'Цыц', 'цыц')
 
def reply_validator(message):
    if message.reply_to_message == None:
        return False
    elif message.text in restricted_messages:
        return True

      
@bot.message_handler(func=reply_validator, content_types=['text'])
def set_ro(message):
    print(message.from_user.language_code)
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time()+300)
    bot.send_message(message.chat.id, strings.get(get_language(message.from_user.language_code)).get("ro_msg"),
                     reply_to_message_id=message.message_id)

@bot.message_handler(commands=['start'], func=lambda message: message.chat.id)
def start(message):
    bot.send_message(message.chat.id, "Что тебе нужно, человечушка ничтожный, если что я здесь /help")
@bot.message_handler(commands=['help'], func=lambda message: message.chat.id)
def start(message):
    bot.send_message(message.chat.id, "Ну и нахуя ты это нажал а? Ладно если хочешь знать, то я много чего умею ,ха, ладно ладно я же Заец, напиши: 'ЗАЕЦ ГОЛОС', 'Заец как закрыть сессию?', 'ЗАЕЦ ПРИВЕТ'. Могу устраивать БУНД и АНТИБУНД. Блокирую народ по проcьбе адинистрации. Вызываю Антонюка ВАХАХАХАХАХ. Все услуги по скидкам с пиздюлями.")    
@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'ЗАЕЦ ГОЛОС')
def handle_text(message):
    bot.send_message(message.chat.id, random_message())
    
@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'Заец как закрыть сессию?')
def handle_text(message):
    bot.send_message(message.chat.id, random_message1())

@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'ЗАЕЦ ПРИВЕТ')
def handle_text(message):
    bot.send_message(message.chat.id, random_message3())

@bot.message_handler(content_types=['text'])
def handle_text(message):
   if message.text == "БУНД": 
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOXt4c5XskqBxa1vnyhszgcCyRZEnKftnyWZgKcFguPYdeUOLx'
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg','rb')
    bot.send_chat_action(message.chat.id,'upload_photo')           
    bot.send_photo(message.chat.id, img)
    img.close()
   elif message.text == "АНТИБУНД":
    url = 'https://301-1.ru/important-memes/img/2018_04_19_16_04_38_a142140e6d98001dc172a5b1f8a73328.jpg'
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg','rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')           
    bot.send_photo(message.chat.id, img)
    img.close()
                                    

        
if __name__ == "__main__":
    bot.polling(none_stop=True)
