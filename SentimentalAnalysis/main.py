import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from PyQt5.QtWidgets import QApplication
from SentimentalAnalysis.MachineLearning.Predictor import predict
from SentimentalAnalysis.MachineLearning.Build import train_model
from SentimentalAnalysis.UI.Interface import App


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
