import math

def fibonacci(n):
	''' Return the nth fibonacci number
	'''
	golden_ratio = (1 + math.sqrt(5)) / 2
	return round((golden_ratio**n) / math.sqrt(5))

def numDigits(n):
	''' Return the number of digits n contains
	'''
	return strCount(str(n))

def strCount(n):
	''' Count the number of strings in n
	'''
	if len(n) <= 2:
		return len(n)
	else:
		if len(n) % 2 == 1:
			return strCount(n[0:(1+len(n))/2]) + strCount(n[(1+len(n))/2:len(n)])
		else:
			return strCount(n[0:(len(n)/2)]) + strCount(n[(len(n)/2):len(n)])

def fibDigits(n):
	''' Return the first fibonacci number with n digits
	'''
	a = 1
	while numDigits(fibonacci(a)) < n:
		a += 1
	print a
	return a

fibonacci(12)
fibDigits(3)
fibDigits(5)
fibDigits(99)