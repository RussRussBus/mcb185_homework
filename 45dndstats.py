# 45dndstats.py by Russell Hong

import random

# 3D6
total = 0
print('3D6')
for stat in range(6):
	stat = 0
	for dr in range(3): # dr stands for dice roll
		dr = random.randint(1, 6)
		stat += dr
	total += stat
	print(stat)
print('average =', total/6)
print()

# 3D6r1
total = 0
print('3D6r1')
for stat in range(6):
	count = 0
	stat = 0
	while count < 3:   # loop can only end when count = 3
		dr = random.randint(1, 6)
		if dr != 1:
			stat += dr
			count += 1 # count can only increase when dice does not roll 1
	total += stat
	print(stat)
print('average =', total/6)
print()

# 3D6x2
total = 0
print('3D6x2')
for stat in range(6):
	stat = 0
	for dr in range(3):
		dr = random.randint(1, 6)
		dr += random.randint(1, 6)
		if stat < dr: # only takes the biggest pair
			stat = dr
	total += stat
	print(stat)
print('average =', total/6)
print()

# 4D6d1
total = 0
print('4D6d1')
for stat in range(6):
	stat = 0
	low = 0 # keeps track of lowest number of the 4 dice rolls
	for dr in range(4):
		dr = random.randint(1, 6)
		if low == 0 or low > dr: # 1st condition is used to initially assign low to dr
			stat += low
			low = dr
		else:
			stat += dr
	total += stat
	print(stat)
print('average =', total/6)