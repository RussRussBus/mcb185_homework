# 32fibonacci.py by Russell Hong

num1 = 0
num2 = 1
print(num1)        # prints the first 2 numbers of the sequence
print(num2)

for n in range(8): # range is set to 8 because first 2 numbers are already displayed
	if n % 2 == 0: # even numbers
		num1 = num1 + num2
		print(num1)
	else:          # odd numbers
		num2 = num1 + num2
		print(num2)