# 52entropy.py by Russell Hong

import sys
import math

prob = list()
total = 0
h = 0
for n in sys.argv[1:]:
	f = float(n)
	if f <=0 or f >= 1: sys.exit('not a probability')
	prob.append(f)
for n in prob:
	total += n
if total != 1: sys.exit('probabilites do not sum to 1')
for n in prob:
	h -= n * math.log2(n)
print(h)
