import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from EmployeeSatisfaction.src.Brain import Model
from EmployeeSatisfaction.src.GUI.Interface import App
from PyQt5.QtWidgets import QApplication


value = sys.argv[1]
if value == "train":
	Model.Train()
elif value == "gui":
	app = QApplication(sys.argv)
	val = App()
	sys.exit(app.exec_())




