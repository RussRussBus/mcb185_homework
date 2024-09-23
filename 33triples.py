# 33triples.py by Russell Hong

a = 1
b = 1
counter = 0

for i in range(0,100):
	for j in range(0,99):        # range is set to 99 so b < 100
		c = (a**2 + b**2)**.5
		if c % 1 == 0 and a < b:
			counter = counter + 1
			print(a, b, c)
		b = b + 1
	a = a + 1
	b = 1
print(counter)