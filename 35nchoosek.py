# 35nchoosek.py by Russell Hong

# factorial function
def factorial(n):
	total = 1
	for i in range(0, n):
		i = i + 1
		total = i * total
	return total

def nck(n, k):
	total = factorial(n) / (factorial(k) * factorial(n - k))
	return total

print(nck(10, 3))
print(nck(0, 0))
print(nck(100, 453))
print(nck(44, 30))
print(nck(9, 0))
print(nck(0, 3))