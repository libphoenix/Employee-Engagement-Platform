from DataCleaning import clean_and_load
import pandas as pd
import numpy as np
import constants as cn


print("Program Started")
# loadng data
print("File loading...", end = "&")
data_type = {'clean_text': str, 'category': int}
datastore = clean_and_load(cn.file_path, data_type)
print("... done")

#spliting dataset 
print("Spliting dataset....",end = "&")
training_set = int(datastore.shape[0] * cn.training_percent)

training_df = datastore[:training_set]
testing_df = datastore[training_set:]
training_sentences = training_df.clean_text.to_numpy()
training_lables = training_df.category.to_numpy()

testing_sentences = testing_df.clean_text.to_numpy()
testing_lables = testing_df.category.to_numpy()
print(".... done")

# data preprocessing
print("Data per-processing....", end = "&")
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(oov_token = '<oov>', lower = False, split = ' ')
tokenizer.fit_on_texts(training_sentences)

training_sequence = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequence, maxlen = cn.max_length,padding = 'post', truncating = 'post')

testing_sequence = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequence, maxlen = cn.max_length,padding = 'post', truncating = 'post')

training_padded = np.array(training_padded)
training_lables = np.array(training_lables)
testing_padded = np.array(testing_padded)
testing_lables = np.array(testing_lables)
print(".... done")

#Building model 
print("Creating model....")
from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Embedding(input_dim = len(tokenizer.word_index),output_dim = cn.embedding_dim, input_length = cn.max_length),
    layers.GlobalAveragePooling1D(),
    layers.Dense(24,activation = 'relu'),
    layers.Dense(3, activation= 'relu')
    ])

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

model.summary()

print(".... Done")

# Traning model
print("Training model....")

model.fit(training_padded, training_lables, epochs = cn.num_epochs, validation_data = (testing_padded, testing_lables))
print("...Training done")

model.save("Trained_model")