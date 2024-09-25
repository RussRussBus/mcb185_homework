# 41zscores.py by Russell Hong

import random

limit = 100000

z1 = 0
z2 = 0
z3 = 0

for i in range(limit):
	r = random.gauss(0.0, 1.0)
	r = abs(r) # accounts for both negative and positive values
	if r > 1: z1 = z1 + 1
	if r > 2: z2 = z2 + 1
	if r > 3: z3 = z3 + 1

# finding above the mean
z1 = 1 - z1/limit
z2 = 1 - z2/limit
z3 = 1 - z3/limit

print(z1, z2, z3)
