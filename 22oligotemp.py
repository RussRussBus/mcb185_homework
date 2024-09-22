# 22oligotemp.py by Russell Hong
# returns the melting temperature of given oligo

def oli_temps(A, T, G, C):
	if A + T + G + C <= 14: Tm = (A + T) * 2 + (G + C) * 4
	else: Tm = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
	return Tm
	
print(oli_temps(10, 4, 30, 9))
print(oli_temps(1, 4, 3, 4))
print(oli_temps(0, 0, 0, 0))
print(oli_temps(310, 433, 344, 100))