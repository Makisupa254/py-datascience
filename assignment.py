
import csv

def read_file(filename):
	lines = []
	with open(filename, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			lines.append(line)
	return lines

a = read_file("NBA 14-15 Game Log.csv")
	
def print_csv(data):
	for line in data:
		print line

# Return the number of lines in the data file (exclude the headers)
def prob_01(data):
	count = 0
	for row in data:
		count += 1
	return count
print(prob_01(a))

# Get the name of the first player in the file
def prob_02(data):
	name = a[0]
	return name
print(prob_02(a))
	
# Get the date on the last line in the file
def prob_03(data):
	date = lines[DATE]
	return date
	
# Get the 100th player's name
def prob_04(data):
	
	return name

# Get a list of the unique OWN_TEAM elements in the file
def prob_05(data):
	teams = []
	
	return teams