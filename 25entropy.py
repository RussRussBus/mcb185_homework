# 25 entropy.py by Russell Hong

import math

def entropy(a, t, c, g):
	total = a + t + c + g                           # obtains the total number of events
	shan_entropy = total * (.25 * math.log2(1/.25))
	return shan_entropy
	
print(entropy(1, 1, 1, 1))
print(entropy(0, 0, 0, 0))
print(entropy(10, 12, 30, 61))
print(entropy(100, 30, 40, 50))