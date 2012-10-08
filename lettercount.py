from sys import argv

script, file = argv
import string
# filename variable
# read lines in file

# get letter count

# define function to count letters, pass filename as arg
def lettercount(filename):
	counter = 0
	# create list with letters of the alphabet for comparison
	alphabet_list = list(string.ascii_lowercase)

	# list to hold number of times each letter occurs
	alphabet_count = [0]
	alphabet_count = alphabet_count*26

	open_file = open(filename)
	# store file contents in text, convert to lower case
	text = open_file.read()
	text.lower()

	# loop through alphabet list 

	for letter in text:
		indexnumber= ord(letter)-97
		if indexnumber >= 0 and indexnumber < 26:
			alphabet_count[indexnumber]+= 1
		

	
	for count in alphabet_count:
		print count
	print len(alphabet_count)



lettercount(file)

