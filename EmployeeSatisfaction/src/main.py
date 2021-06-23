import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from EmployeeSatisfaction.src import Stats, Brain
from EmployeeSatisfaction.src.GUI.Interface import App
from PyQt5.QtWidgets import QApplication


value = sys.argv[1]
if value == "train":
	if sys.argv[2] == "NN":
		Brain.Model.TrainNeuralNetwork()
	elif sys.argv[2] == "RF":
		Brain.Model.TrainRandomForest()
elif value == "gui":
	app = QApplication(sys.argv)
	val = App()
	sys.exit(app.exec_())
elif value == "predict":
	if sys.argv[2] == "RF":
		Brain.Model.PredictLargeDataRandomForest()
elif value == "stats":
	Stats.displayStats()




