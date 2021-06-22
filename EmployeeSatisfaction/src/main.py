import os
import sys

from pandas.core.algorithms import mode
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from EmployeeSatisfaction.src.Brain import Model
from EmployeeSatisfaction.src.GUI.Interface import App
from PyQt5.QtWidgets import QApplication


value = sys.argv[1]
if value == "train":
	if sys.argv[2] == "NN":
		Model.TrainNeuralNetwork()
	elif sys.argv[2] == "RF":
		Model.TrainRandomForest()
elif value == "gui":
	app = QApplication(sys.argv)
	val = App()
	sys.exit(app.exec_())




