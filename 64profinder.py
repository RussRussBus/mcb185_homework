# 64profinder.py by Russell Hong

import c_dogma as dogma
import gzip
import sys

file = sys.argv[1]
len_limit = int(sys.argv[2])
p_count = 0							 # tracks the number of proteins

seq = []                             # list allows appending of each line
with gzip.open(file, 'rt') as fp:
	for line in fp:
		if '>' in line: 
			fp_title = line			 # allows title to be printed later
			continue
		line = line.replace('\n','') # gets rid of new line
		seq.append(line)
	og_seq = ''.join(seq)

# edits the title to look like assignment
fp_title = fp_title.split()
fp_title = str(fp_title[0])

# runs program 3 times, once per reading frame for each strand
r_comp = dogma.revcomp(og_seq) # finds reverse compliment of seq
for i in range(3):
	seq = og_seq[i:]		   # seq based on reading frame
	r_seq = r_comp[i:]
	prot_ls = []

	# picks between forward and reverse strand
	for i in range(2):
		if i == 0:   c_seq = seq # c_seq = current sequence
		elif i == 1: c_seq = r_seq
		# finds proteins in strand
		ls_aa = []
		for n in range(0, len(c_seq), 3):
			codon = c_seq[n:n+3]
			aa = dogma.translate(codon) # gets amino acid
			# checks to see if amino acid is a stop seq
			if aa == '*':
				counter = 0
				ls_aa.append(aa)
				for i in range(len(ls_aa)): # makes sure protein starts with M
					if ls_aa[i] == 'M': break
					else: counter += 1
				ls_aa = ls_aa[counter:]		# removes any aa before start codon
				ls_aa = ''.join(ls_aa)
				if len(ls_aa) >= len_limit: # checks length of protein
					prot_ls.append(ls_aa)
					ls_aa = []				# empty ls to allow for processing next prot
				else: ls_aa = []
			else: ls_aa.append(aa)			# adds aa to ls if not stop codon

		# prints the output for every protein
		for prot in prot_ls:
			print(f'{fp_title}-prot-{p_count} \n {prot}')
			p_count += 1