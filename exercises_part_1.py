#1
#a. Sort the list below alphabetically
#b. The sorted list should be in Alphabetical order 
list_unordered = ['Sensational', 'troops', '2ndIINone', 'Laquan', 'B52s', 'GZA', 'Kool Keith', 'Lupe Fiasco', 'Aceyalone']

#2
#a. remove all non numbers and non letters from list elements
list_with_extra_stuff = ['j7627!', 'tr00ps', '45 king', 'Ja55y J3FF', '%431jhg', '#BEEF', 'wUT4Cl3an!']

#3
#Construct a function to use regex to:
#a. Pull out first names that begin with J and end with n
#b. Put those names is a dictionary called winners, where the last name is the value of the key
#c. words passed in are of the form '<FIRST_NAME> <LAST_NAME>' (shown on line 23)
def regex_stuff(*words):
	winners = {}
	for word in words:
	 	regex_match = re.search(r'(<REGEX_GOES_HERE>', word)
	 	if regex_match:
	 		winners[regex_match.group(1)] = regex_match.group(2)
	return winners

print(regex_stuff('Bobby Jindall','Juan Martin','Avon Foru','Aaron Nolan','Jaila Stevens','Awan Code', 'Julian Assage'))

#4 Write a function to do the following
#a. Use the line of code below to generata a random number.
	#rando = random.randint(1, 10000000)
#b. If the number is below 5000, print 'Audi'
#c. If the number is above 1000000 print 'Daddy Warbucks'
#d. If the number is above 5000000 print 'Double your score'

def number_slogan_generator():
	rando = random.randint(1, 10000000)
	#code goes here to examine number and print appropriate slogan


#5 Return the list without negative values
	list_of_numbers = [-1,3,4,5,-9,100,-45]

