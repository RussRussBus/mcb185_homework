# 43randomdna.py by Russell Hong

import random

seq_num = 10

for i in range(seq_num):
	print(f'>seq-{i+1}')
	length = random.randint(50, 60)
	for i in range(length):
		print(random.choice('ATCG'), end = '')
	print()