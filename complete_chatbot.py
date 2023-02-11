# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:09:56 2021

@author: Madi
"""


import random
import json
import pickle
import numpy as np
import nltk


bot_name = "Car Assistant"



from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
# In order to load the moddel we need to import the function load_model

lemmatizer= WordNetLemmatizer()
intents=json.loads(open('intents.json').read())

# We need to load words, classes, and models
words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))

model = load_model('chatbot_model.h5')

# Function for cleaning up the sentences.
def clean_up_sentence(sentence):
    sentence_word= nltk.word_tokenize(sentence)
    # After tokenize the sentence we are going to lemmatize the word.
    sentence_word=[lemmatizer.lemmatize(word) for word in sentence_word]
    return sentence_word

# Function for getting the bag of words.
# this function will convert a sentence into a bag of words so into a list full of zeros and ones that indicate if the word is there or not so using flex essentially in the some way in the training script.
def bag_of_words(sentence):
    sentence_word=clean_up_sentence(sentence)
    bag=[0]*len(words)                              # Initial bag full of zeros as many as there are individual words
    for w in sentence_word:
        for i, word in enumerate(words):
            if word==w:
                bag[i]=1
    return np.array(bag)

# Function for predicting the class based on the sentences essentially.
def predict_class(sentence):
    bow=bag_of_words(sentence)
    # In order to get the prediction.
    res=model.predict(np.array([bow]))[0]           # res= results [bow]bag of words as list in [0]zero index to match the format
    ERROR_THRESHOLD=0.25
    # Error_Threshold that allows for a certain uncertainty but if that uncertainty is too high we're going to take it into a result
    results=[[i,r]for i,r in enumerate(res)if r>ERROR_THRESHOLD]        # i-> index, r-> result
    # Then we have to sort the result.
    results.sort(key=lambda x:x[1], reverse=True)   # reverse->Decending order
    # The key of sorting is going to be anonymous function a lambda expression
    
# We need to take the first index overtime.
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
  tag = intents_list[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result = random.choice(i['responses'])
      break
  return result