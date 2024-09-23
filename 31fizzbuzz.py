# 31fizzbuzz.py by Russell Hong

for i in range(1,101): # range is 1 to 101 because range stops before end limit
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	elif i % 3 == 0:              print('Fizz')
	elif i % 5 ==0:               print('Buzz')
	else:                         print(i)