# 55colorname.py by Russell Hong

import sys

colorfile = sys.argv[1]
R = sys.argv[2]
G = sys.argv[3]
B = sys.argv[4]
ls_colors = [R, G, B] # puts values into a list for use in dtc function

# finds the difference between the given color value and the color values in the library
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		p = int(p)
		q = int(q)
		d += abs(p - q)
	return d # returns the total difference of all three values

# searches the color library and finds the color that best matches the given color values
min = 0 # keeps track of the lowest total difference value
with open(colorfile) as fp:
	for line in fp:
		line = line.split()
		color_code = line[2]
		color_code = color_code.split(',')
		diff = dtc(color_code, ls_colors)
		if diff < min or min == 0:
			min = diff
			color = line[0]
		
print(color)