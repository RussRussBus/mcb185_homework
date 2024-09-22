# 26phred.py by Russell Hong

# determines if the input is between 0 and 1 or greater than 1
# then calculates either phred score or probability

import math

def phred(num):
	if 0 < num < 1:                  # finds phred score based on probability
		phr = -10 * (math.log10(num))
		return phr
	elif num > 1:                    # finds probability based on phred score
		prob = 10 ** (-num/10)
		return prob
	else: return                     # for any inputs invalid inputs

print(phred(.5))
print(phred(3.010299956639812))
print(phred(0))
print(phred(1))