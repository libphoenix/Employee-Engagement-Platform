import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from SentimentalAnalysis.MachineLearning.Predictor import predict

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'EEP'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.textbox = QTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(600,200)
        
        self.button = QPushButton("Check", self)
        self.button.move(280,220)
        self.button.clicked.connect(self.onClick)

        self.label = QLabel("Sentiment",self)
        self.label.move(50,250)
        self.label.resize(500,200)

        self.statusBar().showMessage("2021 - Imaginea")
        self.show()
    
    @pyqtSlot()
    def onClick(self):
        textboxValue = self.textbox.toPlainText()
        val = predict(textboxValue)
        font = self.font()
        font.setBold(True)
        self.label.setFont(font)
        if float(val[0]) >= 0.5:
            self.label.setText("Sentiment - Satisfied")
            self.label.setStyleSheet("color : green")
        else:
            self.label.setText("Sentiment - Not Satisfied")
            self.label.setStyleSheet("color : red")

        self.textbox.setText("")
