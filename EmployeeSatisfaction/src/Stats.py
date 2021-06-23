from EmployeeSatisfaction.src.Config import data_path
import pandas as pd
import os

def ShowUnique():
	data = pd.read_csv(os.getcwd() + '/' + data_path)
	for row in data:
		print(row)
		print(data[row].unique())

def UpdateData():
	data = pd.read_csv(os.getcwd() + '/' + data_path)
	data['recruitment_type'] = data['recruitment_type'].replace(['Referral', 'WalkIn', 'OnCampus', 'RecruitmentAgency'],['1','2','3','4'])
	data['location'] = data['location'].replace(['Suburb','City'],['2','1'])
	data['Dept'] = data['Dept'].replace(['HR','Technology','Sales','Purchasing','Marketing'],['1','2','3','4','5'])
	data['education'] = data['education'].replace(['PG','UG'],['1','2'])

	print("done modifying")
	del(data["Id"])
	del(data["emp_id"])
	data.to_csv(os.getcwd()+"/Data/"+"data.csv",index=False)

def displayStats():
	data = pd.read_csv(os.getcwd() + '/' + data_path)
	
	print(pd.unique(data["satisfied"]))


