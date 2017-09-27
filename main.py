#!/usr/bin/python
# -*- coding: ascii -*-
import os, sys

import telebot
import constants

bot = telebot.TeleBot(constants.token)
chat2ch = bot.get_chat(-1001009232144)
chatme = bot.get_chat(79563301)

# bot.send_message(79563301, "hello")
print(bot.get_me())

print("\n -----------")


def log(message, answer):
    from datetime import datetime
    print (datetime.now())
    print ("Message from {0} {1}. (id = {2}) \n Text - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)

"""
@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = message.text
    log(message,answer)
    print ("Message sent")
    bot.send_message(message.chat.id, answer)
"""


bot.forward_message(chatme.id, chat2ch.id,12776)



#bot.send_message(79563301,bot.get_chat(-1001009232144))


bot.polling(none_stop=True, interval=0)
