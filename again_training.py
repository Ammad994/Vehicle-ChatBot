# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:09:56 2021

@author: Madi
"""


# For choosing randon response
import random
import json

# For serialization
import pickle
import numpy as np

# Algorithm used
import nltk
import tensorflow as tf


from nltk import word_tokenize,sent_tokenize
from nltk.corpus import wordnet as wn

# its going to reduce the word to its stem so we don't lose any performance because it's looking for the exact word like: work, working, worked, works. It see all those as a same word.
from nltk.stem import WordNetLemmatizer

#For importing simple sequential model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout

# SGD-> Stochastic Gradient descent
from tensorflow.keras.optimizers import SGD

#Now lemmetizing the individual words

# First creating a lemmetizer
lemmatizer = WordNetLemmatizer()
# () For call the constructor of the word lemmetizer

# Have to load json file
intents = json.loads(open('intents.json'). read())

# Now Create 3 new lists
words=[]
classes=[]
documents=[]
ignore_letters=["?","!",".",","]

nltk.download('punkt')

# We have to iterate over the intent
for intent in intents["intents"]:               # Now we have to imagine that this thing here is a dictionary in python so now we have the intent which is the object and then we need to access the key intents and for each intent we have certain subkey and sub values.
    for pattern in intent["patterns"]:
        word_list= nltk.word_tokenize(pattern)
        words.extend(word_list)                 # Extend means taking the content and append to list and append means taking list and apend to list.
        
        # Also we have to append to the documents we are gaoing to append a tuple first of all of the word list and then also as the classes of the class of this particular intent.
        documents.append((word_list, intent['tag']))
        
        # We are going to check if this class is already in the classes list if not we are going to append it to the classes.
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
# For see the result
#print(documents)

nltk.download('wordnet')
# lematize the word for every word in words if this word is not in ignore letter list.
words= [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]

# In order to eleminate the duplicates.
words=sorted(set(words))
# Set eleminates the duplicates and sorted turn it back to the list and sort it.

#for see the result.
#print(words)

# same for classes
classes=sorted(set(classes))

# Now we have to save words in the file.
pickle.dump(words, open("words.pkl",'wb'))      # wb -> writting binary

# and same thing for classes.
pickle.dump(classes, open('classes.pkl', 'wb'))

training=[]                                     # Empty list

# Creating an empty output which is a template of zeros and we need as many zeros as there are classes.
output_empty=[0]*len(classes)
for document in documents:
    bag=[]
    # Create empty bag here so far each of those combinations we're going to create an empty bag of words.
    word_patterns=document[0]
    word_patterns= [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        # For each word we want to know if it occurs in the pattern
        bag.append(1) if word in word_patterns else bag.append(0)
    
    # Same thing for the output.
    output_row= list(output_empty)              # Coping
    output_row[classes.index(document[1])]=1
    
    # Wanna know the class which is at index 1 wanna know the index and then we are going to add to set this index in the output row to one then we are going to append the whole thing to the training list we created.
    training.append([bag, output_row])

# so when we run that loop all the document data is going to be in the trining list and we can work with this training list in order to train the nural network.
# Now one final step of pre processing before we get into building the nural network and this is first of all we're going to shuffle the data.
random.shuffle(training)
training=np.array(training)

# Then split it into X and Y values.
train_x=list(training[:,0])
train_y=list(training[:,1])

# Those are the X and Y values the feature and the labels that we're going to use to train our neural network.

# Neural Network

# Going to create simple sequential model
model= Sequential()

# Going to add couple of layers
# 1st input layer
model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))      # 128->neurons
# Activation function to rectify linear unit

# To prevent overfitting
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation='softmax'))
# Thats the function that sumup or scale the results in the output layer so that they all add upto one so that we have sort of percentages of how likely it is to have that output or result.

# Then we are gaoing to quickly define a stochastic gradient desent(SGD) optimizer
# lr-> learning rate
sgd=SGD(lr=0.01,decay=1e-6, momentum=0.9, nesterov=True)

# Then we compile the model
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# numpy as np remember
hist= model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print("Done")