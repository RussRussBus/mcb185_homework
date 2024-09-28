# 57birthday.py by Russell Hong

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
n_success = 0 # tracks the number of successful trials

# runs a number of times based on trials input
for trial in range(trials):
	
	# creates a list of 0 with the number of days determining the number of items
	calendar = []
	for n in range(days): calendar.append(0)
	
	# randomly adds 1 to an item in the list
	for p in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
	
	"""
	This loop sees if any items in the list are greater than 1, indicating multiple 
	people with the same birthday.
	
	The break avoids double counting trials that have multiple people with multiple bdays.
	"""
	for day in calendar:
		if day > 1:
			n_success += 1
			break
			
print(n_success/trials)