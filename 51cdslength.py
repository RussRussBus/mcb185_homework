# 51cdslength.py by Russell Hong

import gzip

lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'

with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		if line.find('CDS') != -1:
			ls_line = line.split()
			if 'CDS' in ls_line: cds_i = ls_line.index('CDS')
			cds_end = cds_i + 2
			cds_start = cds_i + 1
			ls_line[cds_end] = int(ls_line[cds_end])
			ls_line[cds_start] = int(ls_line[cds_start])
			lengths.append(ls_line[cds_end] - ls_line[cds_start] + 1)
print(lengths)