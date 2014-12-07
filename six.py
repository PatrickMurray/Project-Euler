start	= 1
end	= 100


def sum_of_square (a, b):
	summation = 0
	i = a
	while i <= b:
		summation += i ** 2
		i += 1
	
	return summation


def square_of_sum (a, b):
	n = a + b
	summation = n * (n-1) / 2
	
	return summation ** 2


def difference (a, b):
	return square_of_sum(a, b) - sum_of_square(a, b)


print difference(start, end)
