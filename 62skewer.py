# 62skewer.py by Russell Hong

import c_dogma
import sys
import gzip

file = sys.argv[1]
w = int(sys.argv[2])

# gives sequence as a continuous string without title
seq = []                             # list allows appending of each line
with gzip.open(file, 'rt') as fp:
	for line in fp:
		if '>' in line: continue     # gets rid of title
		line = line.replace('\n','') # gets rid of new line
		seq.append(line)
seq = ''.join(seq)                   # turns list into a string
_____________________________________________________________________________

# fast version of finding gc composition and gc skew
g = 0
c = 0
s = seq[:w]
n_windows = 0 # keeps track of number of windows to determine overall mean of both values
comp_total = 0
skew_total = 0

# finds gc composition and skew for initial window
for nt in s:
	if nt == 'G': g += 1
	if nt == 'C': c += 1
ave = (g+c) / len(s)
comp_total += ave
n_windows += 1
if g+c == 0: skew_total += 0
else:        skew_total += (g-c) / (g+c)

# finds gc composition and skew for every other window
for i in range(len(seq) -w):
	if s[0] == 'G': g -= 1  # ensures that number of G and C is accurate for window
	if s[0] == 'C': c -= 1
	i += 1
	s = seq[i:w+i]		    # moves window
	if s[-1] == 'G': g += 1 # only looks at last nucleotide of window
	if s[-1] == 'C': c += 1
	ave = (g+c) / len(s)
	comp_total += ave
	if g+c == 0: skew_total += 0
	else:        skew_total += (g-c) / (g+c)
	n_windows += 1

# mean of overall gc composition and skew respectively
print(comp_total / n_windows)
print(skew_total / n_windows)
____________________________________________________________________________________

# slow version of finding gc composition and skew
count = 0 # used to find mean of gc composition and skew
comp_total = 0
skew_total = 0
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	count += 1
	comp_total += c_dogma.gc_comp(s)
	skew_total += c_dogma.gc_skew(s)
print(comp_total/count)
print(skew_total/count)