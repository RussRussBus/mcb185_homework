# 23hydropathy.py by Russell Hong
# Get Kyte-Doolittle hydrophobicity value of animo acid letters

# dictionary of values from MCB185 calculating hydropathy section
kdh = {
'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M':  1.9, 'A':  1.8, 
'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
'E': -3.5, 'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5
}

# function that determines if input is an amino acid and returns value if true
def hydropathy(aa):
	if aa in kdh:
		return kdh[aa]
	else:
		return

print(hydropathy('I'))
print(hydropathy('F'))
print(hydropathy('L'))
print(hydropathy('Q'))
print(hydropathy('P'))
print(hydropathy('O')) # outside of amino acid alphabet