# 34scoringmatrix.py by Russell Hong

alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

# for the first row of the alphabet
print('  ', end = ' ')
for c in alphabet:
	print(c, end = '  ')

# creates new line at the end of the first row
print('')

# creates other 4 rows (rows 2-5)
for c in alphabet:
	print(c, end = ' ')
	
	# scoring match or mismatch
	for nt in alphabet:
		if nt == c:
			print(match, end = ' ')
		else:
			print(mismatch, end = ' ')
	print('')