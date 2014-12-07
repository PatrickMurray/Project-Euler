a	= 1
b	= 2
limit	= 4000000


def fibonacci_sum (limit):
	summation = 0
	while b < limit:
		if b % 2 == 0:
			summation += b
		
		temp = a
		a = b
		b += temp
	
	return summation


print fibonacci_sum(limit)
