from numpy import testing
from pandas.core.algorithms import mode
from tensorflow.keras import Sequential, layers, optimizers
import pandas as pd
import numpy as np
import os
from tensorflow.python.keras.optimizer_v2.adam import Adam
from EmployeeSatisfaction.src.Config import *
from tensorflow.keras import models

def Train():
	data = pd.read_csv(os.getcwd() + "/" + data_path )
	lables = data.iloc[: , -1:]
	input = data.iloc[:, :-1]

	train_split = int(len(lables) * split)

	train_input = input.iloc[:train_split]
	train_lable = lables.iloc[:train_split]

	test_input = input.iloc[train_split:]
	test_lable = lables.iloc[train_split:]

	model = Sequential([
		layers.Dense(units=16, input_shape=(len(input.iloc[0]),), activation='relu'),
		layers.Dense(units=32, activation='relu'),
		layers.Dense(units=32, activation='relu'),
		layers.Dense(units=2, activation='sigmoid')
	])

	model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

	model.fit(x = np.array(input), y = np.array(lables), batch_size = 20, epochs=50, verbose=2)

	model.save("Model")



def Predict(data):
	model = models.load_model("Model")
	return model.predict_classes(data)