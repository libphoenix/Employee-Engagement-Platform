import sys
from PyQt5.QtWidgets import QApplication
from MachineLearning.Predictor import predict

from UI.Interface import App


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    # predict("This is awesome so loving movie.")
