# 63dust.py by Russell Hong

import gzip
import math
import sys

# function for finding entropy when given a list of probabilities
def f_entropy(prob):
	h = 0
	for n in prob:
		if n == 0: continue # skips over values that equal 0
		h -= n * math.log2(n)
	return h

file = sys.argv[1]
w = int(sys.argv[2])
entropy = float(sys.argv[3])

# gives sequence as a continuous string
seq = []                             # list allows appending of each line
with gzip.open(file, 'rt') as fp:
	for line in fp:
		if '>' in line: 
			title = line			 # allows title to be printed later
			continue
		line = line.replace('\n','') # gets rid of new line
		seq.append(line)
	seq = ''.join(seq)

# creates a copy of the sequence with each nucleotide as a list
ls_seq =[]
for nt in seq: ls_seq.append([nt])
# print(list(seq)) try later
a = 0
c = 0
g = 0
t = 0
final = []

# determines if 1st window is a low complexity sequence
s = seq[:w]
for nt in s:
	if nt == 'A': a += 1
	if nt == 'T': t += 1
	if nt == 'C': c += 1
	if nt == 'G': g += 1
if f_entropy([a/w, t/w, c/w, g/w]) < entropy:
	counter = 0
	for n in range(w):
		ls_seq[counter] = ['N']
		counter += 1

# determines if a specified window is a low complexity sequence	
i = 0
for n in range(len(seq) -w): # goes through the whole genome

	# makes sure nt counts are accurate for the window
	if s[0] == 'A': a -= 1
	if s[0] == 'T': t -= 1
	if s[0] == 'C': c -= 1
	if s[0] == 'G': g -= 1
	
	i += 1
	s = seq[i:w+i]
	
	# only counts last nucleotide that has been recently added
	if s[-1] == 'A': a += 1
	if s[-1] == 'T': t += 1
	if s[-1] == 'C': c += 1
	if s[-1] == 'G': g += 1
	
	# finds entropy and compares to critical value
	if f_entropy([a/w, t/w, c/w, g/w]) < entropy:
		counter = 0
		for n in range(w):
			ls_seq[i+counter] = ['N']
			counter += 1

# creates list of genome with changed nucleotides and converts to a string
for nt in ls_seq: final += nt
final = ''.join(final)

# output with wrapped lines at 60 characters
print(title)
for n in range(0,len(final),60):
	print(final[n:n+60])