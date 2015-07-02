
import csv

# In this assignment, tests.py will use the read_file function listed below
# and provide you with the data for each of the problems. Be sure to review
# how to access data fields by column header from the lesson in order to
# to complete the assignment.

def read_file(filename):
	lines = []
	with open(filename, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			lines.append(line)
	return lines

data = read_file('data/NBA1415GameLog.csv')
	
def print_csv(data):
	for line in data:
		print line

# Return the number of lines in the data file (exclude the headers)
def prob_01(data):
	count = 0
	for row in data:
		count += 1
	return count
print(prob_01(data))

# Get the name of the first player in the file using the column name (PLAYER FULL NAME)
def prob_02(data):
	for line in data: 
		name = line["PLAYER FULL NAME"]
		return name
print(prob_02(data))
	
# Get the date on the last line in the file using the column name (DATE)
def prob_03(data):
	for line in data:
		date = line["DATE"]
	return date
print(prob_03(data))
	
# Get the 100th player's name using the column name (PLAYER FULL NAME)
def prob_04(data):
	for line in data: 
		if line == data[99]:
			name = line["PLAYER FULL NAME"]
			return name
print(prob_04(data))

# Get an array of the unique OWN_TEAM elements in the file
def prob_05(data):
	teams = []
	uniqueteams = set()
	uniqueteamslist = []
	for row in data:
		teams.append(row["OWN TEAM"])
	uniqueteams = set(teams)
	uniqueteamslist = list(uniqueteams)
	return uniqueteamslist
print(prob_05(data))
