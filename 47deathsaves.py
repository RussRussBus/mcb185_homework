# 47deathsaves.py bt Russell Hong

import random

ndss = 300
deaths = 0
stabilize = 0
revives = 0

for i in range(ndss): # nds = number of death save scenarios
	failure = 0
	success = 0
	while True:
		dr = random.randint(1, 20) # dr = dice roll
		
		if dr == 20: 
			revives += 1
			break
			
		if dr == 1: failure += 2
		if dr < 10: failure += 1
		if failure >= 3:
			deaths += 1
			break
			
		if dr >= 10: success += 1
		if success >= 3:
			stabilize += 1
			break
print('Probability of deaths, stabilizes, and revives given',
ndss, 'number of death save scenarios')
print(deaths/ndss, stabilize/ndss, revives/ndss, sep = '\t')