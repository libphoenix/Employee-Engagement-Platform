import enum

class Dept(enum.Enum):
	HR = 1
	Technology = 2
	Sales = 3
	Purchasing = 4
	Marketing = 5

class Education(enum.Enum):
	PG = 1
	UG = 2

class Location(enum.Enum):
	City = 1
	Suburb = 2

class RecruitmentType(enum.Enum):
	Referral = 1
	WalkIn = 2
	OnCampus = 3
	RecruitmentAgency = 4

class JobLevel(enum.Enum):
	L1 = 1
	L2 = 2
	L3 = 3
	L4 = 4
	L5 = 5

class Rating(enum.Enum):
	x = 1
	xx = 2
	xxx = 3
	xxxx = 4
	xxxxx = 5

class OnSite(enum.Enum):
	Yes = 1
	No = 0

data_path = "Data/EmployeeIndex.csv"
split = 0.8