from pandas.core.algorithms import mode
from tensorflow.keras import Sequential, layers, optimizers
import pandas as pd
import numpy as np
import os
from tensorflow.python.keras.optimizer_v2.adam import Adam
from EmployeeSatisfaction.src.Config import *
from tensorflow.keras import models
import pickle

def TrainNeuralNetwork():
	print("Neural Network")
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

	model.save("NNModel")



def TrainRandomForest():
	from sklearn.ensemble import RandomForestClassifier
	data = pd.read_csv(os.getcwd() + "/" + data_path )
	lables = data.iloc[: , -1:]
	input = data.iloc[:, :-1]

	train_split = int(len(lables) * split)

	train_input = input.iloc[:train_split]
	train_lable = lables.iloc[:train_split]

	test_input = input.iloc[train_split:]
	test_lable = lables.iloc[train_split:]

	model = RandomForestClassifier(random_state=30)
	model.fit(train_input, train_lable)

	testPredction = model.predict(test_input)
	
	from sklearn import metrics

	print("Random forest Accurucy = ", metrics.accuracy_score(test_lable, testPredction))

	pickle.dump(model, open("src/Brain/model.sav",'wb'))

	print("Feature importance")
	feature_list = list(input.columns)
	feature_imps = pd.Series(model.feature_importances_, index=feature_list).sort_values(ascending=False)
	print(feature_imps)




def PredictNeuralNetwork(data):
	model = models.load_model("NNModel")
	return model.predict_classes(data)

def PredictRandomForest(data):
	model = pickle.load(open('src/Brain/model.sav', 'rb'))
	return model.predict(data)