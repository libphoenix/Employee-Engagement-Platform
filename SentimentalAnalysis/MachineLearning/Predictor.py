from tensorflow.keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
import constants as con
from MachineLearning.DataCleaning import remove_url_punctuation_stopwords
import json
import numpy as np

# loading model and dict
model = models.load_model("trained_model")
token_file = open("Data/token.json","r")
word_index = json.load(token_file)
token_file.close()

# def update_token():
#     # creating word index
#     word_index = datasets.imdb.get_word_index()
#     word_index = {k: (v+ 3) for k,v in word_index.items()}
#     word_index["<PAD>"] = 0 
#     word_index["<START>"] = 1
#     word_index["<UNK>"] = 2 # unknown
#     word_index["<UNUSED>"] = 3
#     tf = open("Data/token.json","w")
#     json.dump(word_index, tf)
#     tf.close()

def predict(text):
    tokenized_text = []
    tokenized_text.append(tokenize(remove_url_punctuation_stopwords(text)))
    padded_text = pad_sequences(
        tokenized_text,
        value = word_index["<PAD>"],
        padding = 'post',
        maxlen = con.max_length
    )
    return model.predict(padded_text)

def tokenize(text):
    words = text.split()
    tokenized_text = [word_index["<START>"]]
    for word in words:
        try:
            tokenized_text.append(word_index[word])
        except:
            tokenized_text.append(word_index["<UNK>"])
    return tokenized_text