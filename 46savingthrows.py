# 46savingthrows.py by Russell Hong

import random

simulations = 500

print('simulations:', simulations)

# dc = 5 normally
success = 0
for s in range(simulations):
	dr = random.randint(1, 20)
	if dr >= 5:
		success += 1
pos5 = success/simulations

# dc = 5 advantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr >= 5:
			success += 1
			break # prevents 2nd roll is 1st roll is over dc
pos5a = success/simulations

# dc = 5 disadvantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr <= 5:                # makes result = n if dice roll is below dc
			result = 'n'
			break                  # does not roll 2nd die if 1st roll is below dc
		else: result = 'y'         # makes result = y if dice roll is above dc
	if result == 'y': success += 1 # only successful if result = y
pos5d = success/simulations

# dc = 10 normally
success = 0
for s in range(simulations):
	dr = random.randint(1, 20)
	if dr >= 10:
		success += 1
pos10 = success/simulations

# dc = 10 advantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr >= 10:
			success += 1
			break
pos10a = success/simulations

# dc = 10 disadvantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr <= 10:
			result = 'n'
			break
		else: result = 'y'
	if result == 'y': success += 1
pos10d = success/simulations

# dc = 15
success = 0
for s in range(simulations):
	dr = random.randint(1, 20)
	if dr >= 15:
		success += 1
pos15 = success/simulations

# dc = 15 advantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr >= 15:
			success += 1
			break
pos15a = success/simulations

# dc = 15 disadvantage
success = 0
for s in range(simulations):
	for n in range(2):
		dr = random.randint(1, 20)
		if dr <= 15:
			result = 'n'
			break
		else: result = 'y'
	if result == 'y': success += 1
pos15d = success/simulations

# table of results
print('\t', 'DC = 5', 'DC = 10', 'DC = 15', sep = '\t')
print('normal', '', pos5, pos10, pos15, sep = '\t')
print('advantage', pos5a, pos10a, pos15a, sep = '\t')
print('disadvantage', pos5d, pos10d, pos15d, sep = '\t')