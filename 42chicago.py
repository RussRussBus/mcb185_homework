# 42chicago.py by Russell Hong

import random
import sys

games = 1000000
"""
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')
			
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score)
"""
log = games // 100
total = 0
zeros = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}')
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeros += 1
	total += score
print(total / games)
print(zeros / games)