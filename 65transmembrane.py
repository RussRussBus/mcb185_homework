# 65transmembrane.py by Russell Hong

import sys
import gzip

file = sys.argv[1]

prot_ls = []
fp_title = []
c_prot = []
with gzip.open(file, 'rt') as fp:
	for line in fp:
		line = line.replace('\n','') # gets rid of new line
		if '>' in line:				 # this also indicates new protein so used as divider
			fp_title.append(line)
			c_prot = ''.join(c_prot) # c_prot stores the current protein
			prot_ls.append(c_prot)	 # adds whole protein to protein list
			c_prot = []
		else: c_prot.append(line)
c_prot = ''.join(c_prot) # adds the last protein to protein list
prot_ls.append(c_prot)
prot_ls = prot_ls[1:]	 # gets rid of empty str from the 1st run of appending c_prot

# got list for wikipedia, for reference
'''
hydrophobicity = [['I', 4.5], ['V', 4.2], ['L', 3.8], ['F', 2.8], ['C', 2.5], ['M', 1.9],
['A', 1.8], ['G', -0.4], ['T', -0.7], ['S', -0.8], ['W', -0.9], ['Y', -1.3], ['P', -1.6],
['H', -3.2], ['E', -3.5], ['Q', -3.5], ['D', -3.5], ['N', -3.5], ['K', -3.9], ['R', -4.5]]
'''

# each aa position corresponds to the value of the same position
hp_aa = 'IVLFCMAGTSWYPHEQDNKR'
hp_value = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2,
-3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

# calculates average KD value of a given peptide
def ave_KD(peptide):
	kd = 0	
	for aa in peptide:
		kd += hp_value[hp_aa.find(aa)]
	kd = kd / len(peptide)
	return kd

# finds signal peptide(sp)
counter = 0 # used to relate name for protein to peptide
sp_prot = []
for prot in prot_ls:
	beg = prot[:30] # beg is the beginning 30 aa of the peptide
	for n in range(len(beg)-7):
		sp = beg[n:n+8] 		# finds signal peptide in 8 aa windows
		if ave_KD(sp) >= 2.5:
			if sp.find('P') != -1: break		# makes sure there is no proline in sp
			t_prot = [fp_title[counter], prot]	# links name with protein
			t_prot = ' '.join(t_prot)			# t_prot means temporary protein
			sp_prot.append(t_prot)
			break
	counter += 1

# finds transmembrane region of proteins with signal peptide
tm_prot = []
for prot in sp_prot:
	end = prot[prot.find(' ')+1:]	# breaks apart name with protein
	end = end[31:]					# starts at 31 because aa after 30
	for n in range(len(end)-10):
		tmr = end[n:n+11]			# tmr is transmembrane region
		if ave_KD(tmr) >= 2.0:
			if tmr.find('P') != -1: break
			tm_prot.append(prot)	# appends with protein name and sequence
			break

for prot in tm_prot:
	print(prot)

