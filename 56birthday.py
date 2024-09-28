# 56birthday.py by Russell Hong

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
n_success = 0	# number of successes

for n in range(trials):
	
	# generates a specified number of bdays and puts them in a list
	ls_bday = []
	for p in range(people):
		bday = random.randint(0,days)
		ls_bday.append(bday)

	# finds if there are same bdays
	same = 0      # tracks the number of same bdays in the group
	root_bday = 0 # tracks the bday that is being compared
	for bd in ls_bday:
		count = 0 # tracks the bday that is compared to the current bday
		
		"""
		This open loop will break when the bday that is being compared (n) to is compared 
		to itself (when n = count) to prevent counting itself as a match and prevents 
		unnecessary double counting
		"""
		while True:
			if root_bday == count: break
			if ls_bday[root_bday] == ls_bday[count]:
				same += 1
				break
			count += 1
		root_bday += 1
	if same > 0: n_success += 1
print(n_success/trials)