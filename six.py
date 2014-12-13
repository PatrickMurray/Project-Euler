"""

Sum Square Difference
---------------------
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

"""

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
