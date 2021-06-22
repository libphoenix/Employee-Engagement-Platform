import sys
from PyQt5.QtWidgets import QApplication
from MachineLearning.Predictor import predict
from MachineLearning.Build import train_model

from UI.Interface import App


value = sys.argv[1]

if value == "train":
    train_model()
elif value == "gui":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
elif value == "perdict":
    print("Enter a review: \n")
    text = input()
    print(predict(text))
