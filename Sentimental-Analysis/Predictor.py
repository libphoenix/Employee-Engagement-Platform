from tensorflow.keras import models, datasets
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import constants as con
import json


# loading model and dict

model = models.load_model("trained_model")
token_file = open("Data/token.json","r")
word_index = json.load(token_file)
tokenizer = Tokenizer(num_words = con.vocab_size)
tokenizer.word_index = word_index


# pre processing input data
sentence = ["This movie is awesome. must watch"]

tokenized_sentence = tokenizer.texts_to_sequences(sentence)
padded_sentence = pad_sequences(
    tokenized_sentence,
    value = word_index["<PAD>"],
    padding = 'post',
    maxlen = con.max_length
)
print(model.predict(padded_sentence))



# creating word index
# word_index = datasets.imdb.get_word_index()
# word_index = {k: (v+ 3) for k,v in word_index.items()}
# word_index["<PAD>"] = 0 
# word_index["<START>"] = 1
# word_index["<UNK>"] = 2 # unknown
# word_index["<UNUSED>"] = 3
# tf = open("token.json","w")
# json.dump(word_index, tf)
# tf.close()