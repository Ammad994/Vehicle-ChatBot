# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:56:22 2021

@author: Madi
"""

import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
   r.adjust_for_ambient_noise(source, duration=0.9)
   print("Speak : ")
   audio=r.listen(source)
        
   try:
       text= r.recognize_google(audio)
       #print("you said : ",text)
            
   except:
       print("Sorry could not understand please speak again")
       
        