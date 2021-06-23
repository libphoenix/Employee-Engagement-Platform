import sys
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot
from EmployeeSatisfaction.src.Brain import Model
from EmployeeSatisfaction.src.Config import *
import numpy as np


def start():
	pass

class App(QMainWindow):

	widgetHeight = 30
	widgetPadding = 30



	def __init__(self):
		super().__init__()
		self.title = 'EEP'
		self.left = 200
		self.top = 100
		self.width = 820
		self.height = 760
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Title
		self.titleLable = QLabel(self)
		self.titleLable.move(310, 10)
		self.titleLable.resize(200, self.widgetHeight)

		font = self.font()
		font.setBold(True)
		font.setPixelSize(20)
		self.titleLable.setFont(font)


		if sys.argv[2] == "RF":
			self.titleLable.setText("Random Forest")
		elif sys.argv[2] == "NN":
			self.titleLable.setText("Neural Network")

		# age
		self.ageLable = QLabel(self)
		self.ageLable.move(20, 1 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.ageLable.resize(75,self.widgetHeight)
		self.ageLable.setText("Age")
		self.ageBox = QLineEdit(self)
		self.ageBox.move(200, 1 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.ageBox.resize(150, self.widgetPadding)
		self.ageBox.setMaxLength(2)
		self.ageBox.setValidator(QIntValidator())

		# Department
		self.DeptLable = QLabel(self)
		self.DeptLable.move(20, 2 * (self.widgetHeight + self.widgetPadding) + 20)
		self.DeptLable.resize(75,self.widgetHeight)
		self.DeptLable.setText("Department")
		self.DeptBox = QComboBox(self)
		self.DeptBox.addItems(Dept.__members__)
		self.DeptBox.move(200, 2 * (self.widgetHeight + self.widgetPadding) + 20)
		self.DeptBox.resize(150, self.widgetHeight)

		# location
		self.locationLable = QLabel(self)
		self.locationLable.move(20, 3 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.locationLable.resize(75, self.widgetHeight)
		self.locationLable.setText("Location")
		self.locationBox = QComboBox(self)
		self.locationBox.addItems(Location.__members__)
		self.locationBox.move(200, 3 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.locationBox.resize(150, self.widgetHeight)
		
		# education 
		self.educationLable = QLabel(self)
		self.educationLable.move(20, 4 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.educationLable.resize(75, self.widgetHeight)
		self.educationLable.setText("Education")
		self.educationBox = QComboBox(self)
		self.educationBox.addItems(Education.__members__)
		self.educationBox.move(200, 4 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.educationBox.resize(150, self.widgetHeight)	


		# recruitment type 
		self.recruitmentLable = QLabel(self)
		self.recruitmentLable.move(20, 5 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.recruitmentLable.resize(75, self.widgetHeight)
		self.recruitmentLable.setText("Recruitment Type")
		self.recruitmentBox = QComboBox(self)
		self.recruitmentBox.addItems(RecruitmentType.__members__)
		self.recruitmentBox.move(200, 5 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.recruitmentBox.resize(150, self.widgetHeight)

		# Job_level 
		self.jobLable = QLabel(self)
		self.jobLable.move(20, 6 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.jobLable.resize(75, self.widgetHeight)
		self.jobLable.setText("Job Level")
		self.jobBox = QComboBox(self)
		self.jobBox.addItems(JobLevel.__members__)
		self.jobBox.move(200, 6 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.jobBox.resize(150, self.widgetHeight)

		# rating 
		self.ratingLable = QLabel(self)
		self.ratingLable.move(20, 7 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.ratingLable.resize(75, self.widgetHeight)
		self.ratingLable.setText("Rating")
		self.ratingBox = QComboBox(self)
		self.ratingBox.addItems(Rating.__members__)
		self.ratingBox.move(200, 7 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.ratingBox.resize(150, self.widgetHeight)

		# Onsite
		self.onSiteLable = QLabel(self)
		self.onSiteLable.move(20, 8 *(self.widgetHeight + self.widgetPadding) + 20)
		self.onSiteLable.resize(75, self.widgetHeight)
		self.onSiteLable.setText("On Site")
		self.onSiteBox = QComboBox(self)
		self.onSiteBox.addItems(OnSite.__members__)
		self.onSiteBox.move(200, 8 * (self.widgetHeight + self.widgetPadding) + 20)
		self.onSiteBox.resize(150, self.widgetHeight)

		# Awards 
		self.awardsLable = QLabel(self)
		self.awardsLable.move(20, 9 *(self.widgetHeight + self.widgetPadding) + 20)
		self.awardsLable.resize(75, self.widgetHeight)
		self.awardsLable.setText("Awards")
		self.awardsBox = QLineEdit(self)
		self.awardsBox.move(200, 9 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.awardsBox.resize(150, self.widgetHeight)
		self.awardsBox.setValidator(QIntValidator())
		self.awardsBox.setMaxLength(3)

		# Certification 
		self.certificateLable = QLabel(self)
		self.certificateLable.move(20, 10 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.certificateLable.resize(75, self.widgetHeight)
		self.certificateLable.setText("Certification")
		self.certificateBox = QLineEdit(self)
		self.certificateBox.move(200, 10 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.certificateBox.resize(150, self.widgetHeight)
		self.certificateBox.setValidator(QIntValidator())
		self.certificateBox.setMaxLength(3)

		# Salary
		self.salaryLable = QLabel(self)
		self.salaryLable.move(450, 1 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.salaryLable.resize(75, self.widgetHeight)
		self.salaryLable.setText("Salary")
		self.salaryBox = QLineEdit(self)
		self.salaryBox.move(560, 1 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.salaryBox.resize(150, self.widgetHeight)
		self.salaryBox.setMaxLength(10)
		self.salaryBox.setValidator(QIntValidator())


		# Age in Company
		self.ageInCompanyLable = QLabel(self)
		self.ageInCompanyLable.move(450, 2 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.ageInCompanyLable.resize(100, self.widgetHeight)
		self.ageInCompanyLable.setText("Age in Company")
		self.ageInCompanyBox = QLineEdit(self)
		self.ageInCompanyBox.move(560, 2 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.ageInCompanyBox.resize(150, self.widgetHeight)
		self.ageInCompanyBox.setMaxLength(2)
		self.ageInCompanyBox.setValidator(QIntValidator())



		# Last Hike %
		self.hikeLable = QLabel(self)
		self.hikeLable.move(450, 3 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.hikeLable.resize(75, self.widgetHeight)
		self.hikeLable.setText("Last Hike %")
		self.hikeBox = QLineEdit(self)
		self.hikeBox.move(560, 3 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.hikeBox.resize(150, self.widgetHeight)
		self.hikeBox.setMaxLength(10)
		self.hikeBox.setValidator(QIntValidator())



		# Weight
		self.weightLable = QLabel(self)
		self.weightLable.move(450, 4 *(self.widgetHeight + self.widgetPadding)+ 20)
		self.weightLable.resize(75, self.widgetHeight)
		self.weightLable.setText("Weight")
		self.weightBox = QLineEdit(self)
		self.weightBox.move(560, 4 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.weightBox.resize(150, self.widgetHeight)
		self.weightBox.setMaxLength(4)
		self.weightBox.setValidator(QIntValidator())

		# Check button
		self.button = QPushButton("Check", self)
		self.button.move(200, 11 * (self.widgetHeight + self.widgetPadding)+ 20)
		self.button.resize(100, self.widgetHeight)
		self.button.clicked.connect(self.check)

		self.button = QPushButton("Clear", self)
		self.button.move(400, 11 * (self.widgetHeight + self.widgetPadding) + 20)
		self.button.resize(100, self.widgetHeight)
		self.button.clicked.connect(self.clear)

		# result
		self.resultLable = QLabel(self)
		self.resultLable.move(500, 500)
		self.resultLable.resize(200, self.widgetHeight)

		self.statusBar().showMessage("2021 - Imaginea")
		self.show()



	@pyqtSlot()
	def clear(self):
		self.ageBox.setText("")
		self.DeptBox.setCurrentIndex(1)
		self.locationBox.setCurrentIndex(1)
		self.educationBox.setCurrentIndex(1)
		self.recruitmentBox.setCurrentIndex(1)
		self.jobBox.setCurrentIndex(1)
		self.ratingBox.setCurrentIndex(1)
		self.onSiteBox.setCurrentIndex(1)
		self.awardsBox.setText("")
		self.certificateBox.setText("")
		self.salaryBox.setText("")
		self.ageInCompanyBox.setText("")
		self.hikeBox.setText("")
		self.weightBox.setText("")
		self.resultLable.setText("")

	@pyqtSlot()
	def check(self):
		data = list()
		data.append(int(self.ageBox.text()))
		data.append(self.DeptBox.currentIndex())
		data.append(self.locationBox.currentIndex())
		data.append(self.educationBox.currentIndex())
		data.append(self.recruitmentBox.currentIndex())
		data.append(self.jobBox.currentIndex())
		data.append(self.ratingBox.currentIndex())
		data.append(self.onSiteBox.currentIndex())
		data.append(int(self.awardsBox.text()))
		data.append(int(self.certificateBox.text()))
		data.append(int(self.salaryBox.text()))
		data.append(int(self.ageInCompanyBox.text()))
		data.append(int(self.hikeBox.text()))
		data.append(int(self.weightBox.text()))
		data = [data]
		value = list()
		if sys.argv[2] == "RF":
			value = Model.PredictRandomForest(np.array(data, dtype=int))
		elif sys.argv[2] == "NN":
			value = Model.PredictNeuralNetwork(np.array(data, dtype=int))
		
		font = self.font()
		font.setBold(True)
		font.setPixelSize(20)
		self.resultLable.setFont(font)
		if value[0] == 0:
			res = "Result - Not Satisfied"
			self.resultLable.setStyleSheet("color : red")
		else:
			res = "Result - Satisfied"
			self.resultLable.setStyleSheet("color : green")
		self.resultLable.setText(res)
