# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:13:08 2021

@author: Madi
"""
from Speech_recognition import text
import pyttsx3
#from Speech_recognition import text

friend= pyttsx3.init()

#print("\n\nEnter quit for exit")
from complete_chatbot import predict_class, get_response, intents,bot_name
while True:
  print("You : ",text)
  message = text
  ints = predict_class(message)
  res = get_response(ints, intents)
  print(bot_name," : ",res)
  friend.say(res)
  friend.runAndWait()
  break
  if message=="quit":
      break
  