# 21max3.py by Russell Hong
# finds the largest number out a series of 3

def largest(a, b, c):
	if a > b and a > c:   return a 
	elif b > c and b > a: return b
	else:                 return c

print(largest(4, 4, 4)) # will return c if all else equal
print(largest(1, 2, 3))
print(largest(1, 2, 2)) # will return c if b and c are equally the largest
print(largest(2, 2, 1)) # will return b if a and b are equally the largest
print(largest(2, 1, 2)) # will return c if a and c are equally the largest
print(largest('blue', 'red', 'orange'))