# 24accuracy.py by Russell Hong
# Finds the F1 score when given the values tp, fp, tn, and fn

def F1_scores(tp, fp, tn, fn):
	
	if tp == 0: return # 0 for tp causes division by zero when calculating score
	
	# finds precision and recall
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	
	# calculates F1 score and returns the value
	score = 2 * ((precision * recall) / (precision + recall))
	return score

print(F1_scores(20,30,40,50))
print(F1_scores(2,0,100,40))
print(F1_scores(0,0,0,0))          # test with all zero values
print(F1_scores(3.5,6.7,5.5,1.13))
print(F1_scores(5,5,5,5))
print(F1_scores(0,0,40,50))
print(F1_scores(0,30,0,50))
print(F1_scores(0,30,40,0))