# 30demo.py by Russell Hong

#while True: print('hello')

"""
i = 0

while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

while i < 3:
	print(i)
	i = i + 1
print('final value', i)

for i in range(1, 10, 3):
	print(i)
print('final value', i)

for c in 'hello':
	print(c)

seq = 'GAATTC'
for nt in seq:
	print(nt)

for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
"""
limit = 4
for i in range(0, limit):
	for j in range(i, limit):
		print(i+1, j+1)
