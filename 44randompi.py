# 44randompi.py by Russell Hong

import random

in_c = 0
total = 0
pi = 0

while True:
	x = random.random()
	y = random.random()
	d = (x**2 + y**2)**.5
	if d < 1:
		in_c += 1
	total += 1
	pi = (4 * in_c) / total
	print(pi) # use to see every iteration

# use to see every 1 million iteration
"""
	if total % 1000000 == 0:
		print(f'in_c {in_c}\ntotal {total}\npi {pi}')
"""