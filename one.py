a	= 3
b	= 5
limit	= 1000


def add_to_limit (n, limit):
	summation = 0
	i = n
	while i < limit:
		summation += i
		i += n
	
	return summation


summation =  add_to_limit(a, limit)
summation += add_to_limit(b, limit)
summation -= add_to_limit(a * b, limit)

print summation
