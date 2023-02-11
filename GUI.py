# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:09:56 2021

@author: Madi
"""

# Description: This is a python program GUI for ChatBot

from tkinter import *
from complete_chatbot import predict_class, get_response, intents,bot_name
import pyttsx3
import speech_recognition as sr

friend= pyttsx3.init()



def ask_bot():
    query=user_input.get()
    ints = predict_class(query)
    res = get_response(ints, intents)
    chatBox.insert(END, 'You : ' + query)
    chatBox.insert(END,bot_name+' : ' +str(res))
    friend.say(res)
    friend.runAndWait()
    user_input.delete(0,END)
    chatBox.yview(End)
    engine.runAndWait()
   
def ask_bot2():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.9)
        audio=r.listen(source)
        
        try:
            text= r.recognize_google(audio)
            #print("you said : ",text)
            
        except:
            print("Sorry could not understand please speak again")
    message = text
    ints = predict_class(message)
    res = get_response(ints, intents)
    res = get_response(ints, intents)
    chatBox.insert(END, 'YOU :' + message)
    chatBox.insert(END,bot_name+':' +str(res))
    friend.say(res)
    friend.runAndWait()
    user_input.delete(0,END)
    chatBox.yview(End)
    engine.runAndWait()
        

root = Toplevel()
root.geometry('500x600')
root.title('Vehicle Bot')
root.iconbitmap(r'C:\Users\Madi\Desktop\Database_vehicle\chatbot.ico')

img=PhotoImage(file=r'C:\Users\Madi\Desktop\Database_vehicle\FInalizing\image2.png')
lblPhoto= Label(root,image=img,bg='lightblue',bd=1,width=444,height=250);
lblPhoto.pack(pady=3)
#lblPhoto.place(bordermode=OUTSIDE, height=270, width=300 , x=100 , y = 5)

frame=Frame(root)
sc=Scrollbar(frame)

chatBox=Listbox(frame, width=78,height=16)
chatBox.config(yscrollcommand=sc.set)
sc.config(command=chatBox.yview)

sc.pack(side=RIGHT,fill=BOTH)
#sc.place(bordermode=OUTSIDE, height=300, width=10 , x=500 , y = 10)
chatBox.pack(side=LEFT,fill=BOTH,pady=10)
#chatBox.place(bordermode=OUTSIDE, height=300, width=400 , x=5 , y = 10)
frame.pack()
#frame.place(bordermode=OUTSIDE, height=300, width=400 , x=5 , y = 10)


user_input= Entry(root,font=('Arial',20),bd=4)
#user_input.pack(fill=BOTH)
user_input.place(bordermode=OUTSIDE, height=50, width=350 , x=5 , y = 545)


btn=Button(root,bg='SteelBlue1',bd=5,activebackground='cyan',fg='white',text='Submit',font=('Arial',15),command=ask_bot)
#btn.pack(pady=10,side=LEFT)
btn.place(bordermode=OUTSIDE, height=50, width=90 , x=355 , y = 545)

btn2=Button(root,bg='navy',bd=5,activebackground='cyan',fg='white',text='Mic',font=('Arial',15),command=ask_bot2)
#btn.pack(pady=10,side=LEFT)
btn2.place(bordermode=OUTSIDE, height=50, width=50 , x=447 , y = 545)

#microphone_btn= PhotoImage(file=r'C:\Users\Madi\Desktop\Database vehicle\FInalizing\image1.png')
#img_label= Label(image=microphone_btn,width=50,height=50)
#img_label.pack(pady=20)

#btn2=Button(root,bg='navy',bd= 5 ,activebackground='lightblue',fg='white',text='mic',font=('Arial',20),command=ask_bot2)
#btn2.pack(pady=10,side=RIGHT)
#btn2.place(bordermode=OUTSIDE, height=50, width=50 , x=447 , y = 545,)
root.mainloop()
