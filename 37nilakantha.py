# 37nilakantha.py by Russell Hong

import math

pi = 3 # starts at 3 because that is the start of the Nilakantha series
n = 2 
for x in range(2000): # higher range increases accuracy
	
	# flips + and - each time in the series
	if x % 2 == 0:
		pi = pi + (4 / (n * (n + 1) * (n + 2)))
	else:
		pi = pi - (4 / (n * (n + 1) * (n + 2)))
	n = n + 2
	
print(pi)
print(math.pi) # compares the estimate to the math fuction
