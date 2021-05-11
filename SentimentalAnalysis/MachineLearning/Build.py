from tensorflow.keras.preprocessing.sequence import pad_sequences
import constants as con
from tensorflow.keras import Sequential, layers, optimizers, datasets
from tensorflow import nn

print("Program Started")


def train_model():
    # getting data from keras
    print("Getting data from keras...")
    (train_data, train_labels), (test_data, test_lables) = datasets.imdb.load_data(num_words = con.vocab_size)

    # word index 

    word_index = datasets.imdb.get_word_index()

    word_index = {k: (v+ 3) for k,v in word_index.items()}
    word_index["<PAD>"] = 0 
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2 # unknown
    word_index["<UNUSED>"] = 3

    print(".... done")

    # Pre-processing 
    print("Preprocessing started....")
    train_data = pad_sequences(train_data, 
                                value = word_index["<PAD>"], 
                                padding = 'post', 
                                maxlen = con.max_length )

    test_data = pad_sequences(test_data,
                                value = word_index["<PAD>"],
                                padding = 'post',
                                maxlen = con.max_length )

    print(".... done")

    print("Bulding model....")

    model = Sequential()
    model.add(layers.Embedding(con.vocab_size, 32))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dense(32, activation = nn.relu))
    model.add(layers.Dense(1, activation = nn.sigmoid))

    print(model.summary())

    model.compile(optimizer = optimizers.Adam(), 
                    loss = 'binary_crossentropy',
                    metrics = ['accuracy'])
    print("building done")

    x_val = train_data[:con.validation]
    partial_x_train = train_data[con.validation:]

    y_val = train_labels[:con.validation]
    partial_y_train = train_labels[con.validation:]

    input("Press any key to train model")

    model.fit(partial_x_train, 
                partial_y_train, 
                epochs = con.num_epochs, 
                batch_size = 512,
                validation_data = (x_val, y_val))

    model.save("trained_model")

    print("training done")
    print("evaluating model")
    res = model.evaluate(test_data, test_lables)
    print(res)

# from DataCleaning import clean_and_load
# import pandas as pd
# import numpy as np
# import constants as cn
# from tensorflow.keras import datasets


# print("Program Started")
# loadng data
# print("File loading...", end = "")
# data_type = {'clean_text': str, 'category': int}
# datastore = clean_and_load(cn.file_path, data_type)
# print("... done")

#spliting dataset 
# print("Spliting dataset....")
# training_set = int(datastore.shape[0] * cn.training_percent)

# training_df = datastore[:training_set]
# testing_df = datastore[training_set:]
# training_sentences = training_df.clean_text.to_numpy()
# training_lables = training_df.category.to_numpy()

# testing_sentences = testing_df.clean_text.to_numpy()
# testing_lables = testing_df.category.to_numpy()


# data preprocessing
# print("Data per-processing....", end = "")
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# tokenizer = Tokenizer(oov_token = '<oov>', lower = False, split = ' ', num_words = cn.vocab_size)
# tokenizer.fit_on_texts(training_sentences)

# training_sequence = tokenizer.texts_to_sequences(training_sentences)
# training_padded = pad_sequences(training_sequence, maxlen = cn.max_length,padding = 'post', truncating = 'post')

# testing_sequence = tokenizer.texts_to_sequences(testing_sentences)
# testing_padded = pad_sequences(testing_sequence, maxlen = cn.max_length,padding = 'post', truncating = 'post')

# training_padded = np.array(training_padded)
# training_lables = np.array(training_lables)
# testing_padded = np.array(testing_padded)
# testing_lables = np.array(testing_lables)
# print(".... done")

#Building model 
# print("Creating model....")
# from tensorflow.keras import layers, models

# model = models.Sequential([
#     layers.Embedding(input_dim = cn.vocab_size,output_dim = cn.embedding_dim, input_length = cn.max_length),
#     layers.GlobalAveragePooling1D(),
#     layers.Dense(24,activation = 'relu'),
#     layers.Dense(3, activation= 'relu')
#     ])

# model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# model.summary()

# print(".... done")

# Traning model
# input("Press any key to start training model...")
# print("Training model....")

# model.fit(training_padded, training_lables, epochs = cn.num_epochs, validation_data = (testing_padded, testing_lables), verbose = 2)
# print("...Training done")

# model.save("Trained_model")