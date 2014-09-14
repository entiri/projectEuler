def triangleNumber(n):
	'''
	Return a triangle number of a given size
	'''
	return (n*(n+1))/2

def divisors(n):
	'''
	Return the number of divisors a given number has
	'''
	a = n
	count = 1
	i = 2
	while a != 1:
		if a % i = 0
			a = a/i
			count += 1
		else:
			i += 1
	return count

def tri(n):
	'''
	Return the first triangle number with more than n divisors 
	'''
	a = 1
	b = triangleNumber(a)
	while divisors(b) < n:
		a += 1
		b = triangleNumber(a)
	return b

print tri(1)
print tri(5)
print tri(10)
print tri(15)
print tri(100)
print tri(150)
print tri(500)


