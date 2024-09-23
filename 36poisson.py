# 36poisson.py by Russell Hong

import math

def poisson_prob(n, k):
	total = n**k * math.e**(-n) / math.factorial(k)
	return total

print(poisson_prob(10,20))
print(poisson_prob(0,20))
print(poisson_prob(10,0))
print(poisson_prob(60,29))
print(poisson_prob(130,25))
print(poisson_prob(0,0))