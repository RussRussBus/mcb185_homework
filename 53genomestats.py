# 53genomestats.py by Russell Hong

import gzip
import sys

path = sys.argv[1]
feature = sys.argv[2]
ls_gstats = []
count = 0
min = 0
max = 0
mean = 0
sd = 0

with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line.find(feature) != -1:
			line = line.split()
			if line[2] != feature: continue
			
			# counts the number of lines with specified feature
			count += 1
				
			# finds the length of the feature and puts them into a list
			stat_start = int(line[3])
			stat_end = int(line[4])
			gstats = stat_end - stat_start + 1
			ls_gstats.append(gstats)
			
			# finds min and max of features
			if min > gstats or min == 0: min = gstats
			if max < gstats or max == 0: max = gstats
			
			# finds mean for use in standard deviation
			mean += gstats
mean = mean/count

# finds standard deviation
for n in ls_gstats:
	sd += (n - mean)**2
sd = (sd/count)**.5

# sorts list in numeric order to find median
ls_gstats.sort()
median = ls_gstats[count//2 + 1]

print(f'number of {feature} = {count}')
print(f'min of {feature} = {min}')
print(f'max of {feature} = {max}')
print(f'mean of {feature} = {mean}')
print(f'sd of {feature} = {sd}')
print(f'median of {feature} = {median}')
