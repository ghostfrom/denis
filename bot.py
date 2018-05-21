# -*- coding: utf-8 -*-

import telebot
from telebot import types 
from telegram import ParseMode
import pywapi

import random
from time import time
import urllib.request as urllib2
otmazki = ['*ТЫ ПИДОР*','*НАХУЙ ПАРЫ*','_Я БУХАТЬ. КТО СО МНОЙ?_','*ШО?*','*Отстань*', '`Вызываю Антонюка`', '*MY DICK IS VERY BIG*']
otmazki1 = ['_В АРМИИ_','`ПРЫГАЙ В ОКНО`','*Здравствуй небо в облаках, здравствуй юность в сапогах...*','*Give me your money*','_Та зачем оно тебе нужно?_', '*Вызываю Антонюка*']
otmazki3 = ['*ИДИ НАХУЙ*', '_Вызываю Антонюка_']
url = [ 'http://memesmix.net/media/created/sw6x30.jpg', 'http://risovach.ru/upload/2012/12/mem/zeleniy-slonik_5943097_orig_.png']
random_message = lambda: random.choice(otmazki)
random_message1 = lambda: random.choice(otmazki1)
random_message3 = lambda: random.choice(otmazki3)
random_url = lambda: random.choice(url)
bot = telebot.TeleBot("549489621:AAHjOvAtZMo-eOvedtl4roEzyXCDHla4h54")
   
@bot.message_handler(commands=['weather'])
def handle_start(message):
    weather_com_result = pywapi.get_weather_from_weather_com('UPXX0016')
    weatherReport ="Погода cегодня - " + weather_com_result['current_conditions']['text'] + " и " + weather_com_result['current_conditions']['temperature'] + "°C в " + weather_com_result['location']['name'] + "." + "\n" + "Чуствуется " + weather_com_result['current_conditions']['feels_like'] + "°C. " + "\nДавление - " + weather_com_result['current_conditions']['barometer']['reading'] + " мм.рт.ст." + "\nУФ-уровень - " + weather_com_result['current_conditions']['uv']['text'] + "\nТочка росы - " + weather_com_result['current_conditions']['dewpoint'] + "°C" + "\nВлажность - " + weather_com_result['current_conditions']['humidity'] + "%" + "\nСкорость ветра - " + weather_com_result['current_conditions']['wind']['speed'] + " км/год" + "\nВидимость - " + weather_com_result['current_conditions']['visibility']+ " км" + "\nФаза луны - " + weather_com_result['current_conditions']['moon_phase']['text'] + "\nПоследнее обновление - " + weather_com_result['current_conditions']['last_updated']   
    bot.send_message(message.chat.id, weatherReport)
    print(weather_com_result)
@bot.message_handler(commands=['weatherweek'])
def handle_start(message):
    weather_com_result = pywapi.get_weather_from_weather_com('UPXX0016')
    weatherReport ="Завтра --- макс- " + weather_com_result["forecasts"][1]["high"] + "°C и мин- " + weather_com_result["forecasts"][1]["low"] + "°C" + "\nПослезавтра --- макс- " + weather_com_result["forecasts"][2]["high"] + "°C и мин- " + weather_com_result["forecasts"][2]["low"] + "°C" + "\nЧерез 2 дня --- макс- " + weather_com_result["forecasts"][3]["high"] + "°C и мин- " + weather_com_result["forecasts"][3]["low"] + "°C" + "\nЧерез 3 дня --- макс- " + weather_com_result["forecasts"][4]["high"] + "°C и мин- " + weather_com_result["forecasts"][4]["low"] + "°C"
    bot.send_message(message.chat.id, weatherReport)
    print(weather_com_result)

@bot.message_handler(commands=['start'], func=lambda message: message.chat.id)
def start(message):
    bot.send_message(message.chat.id, "Что тебе нужно, человечушка ничтожный, если что я здесь /help")
@bot.message_handler(commands=['help'], func=lambda message: message.chat.id)
def start(message):
    bot.send_message(message.chat.id, "`Ну и нахуя ты это нажал, а? Ладно, если хочешь знать, то я много чего умею! Ха! Ладно-ладно, я же Заец напиши: 'ЗАЕЦ ГОЛОС'/ 'ЗАЕЦ ПРИВЕТ' / 'Заец, как закрыть сессию?'. Могу устраивать БУНД и АНТИБУНД. Блокирую народ по проcьбе адинистрации. Вызываю Антонюка! ВАХАХАХАХАХ. Все услуги по скидкам с пиздюлями`", parse_mode=ParseMode.MARKDOWN)    
@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'ЗАЕЦ ГОЛОС')
def handle_text(message):
    bot.send_message(message.chat.id, random_message(), parse_mode=ParseMode.MARKDOWN)
    
@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'Заец, как закрыть сессию?')
def handle_text(message):
    bot.send_message(message.chat.id, random_message1(), parse_mode=ParseMode.MARKDOWN)

@bot.message_handler(content_types=['text'],func=lambda message: message.text == 'ЗАЕЦ ПРИВЕТ')
def handle_text(message):
    bot.send_message(message.chat.id, random_message3(), parse_mode=ParseMode.MARKDOWN)


@bot.message_handler(content_types=['text'])
def handle_text(message):
   if message.text == "БУНД": 
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOXt4c5XskqBxa1vnyhszgcCyRZEnKftnyWZgKcFguPYdeUOLx'
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg','rb')
    bot.send_chat_action(message.chat.id,'upload_photo')           
    bot.send_sticker(message.chat.id, img)
    img.close()
   elif message.text == "АНТИБУНД":
    url = 'https://301-1.ru/important-memes/img/2018_04_19_16_04_38_a142140e6d98001dc172a5b1f8a73328.jpg'
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg','rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')           
    bot.send_sticker(message.chat.id, img)
    img.close()
   elif message.text == "Спокойной ночи":
    url = 'http://memesmix.net/media/created/sw6x30.jpg'
    urllib2.urlretrieve(url, 'url_image.jpg')
    img = open('url_image.jpg','rb')
    bot.send_chat_action(message.chat.id, 'upload_photo')           
    bot.send_sticker(message.chat.id, img)
    img.close()                                 

        
if __name__ == "__main__":
    bot.polling(none_stop=True)
