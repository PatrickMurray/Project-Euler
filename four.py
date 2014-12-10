"""

Largest Palindrome Product
--------------------------
Problem 4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Approach
--------
Let:
	digits	= 3
	lower	= 10 ^ (digits - 1)	= 10^2	= 100
	upper	= 10 ^ digits		= 10^3	= 1000

Steps:
1.)	Loop through every number "i" in the domain [lower, upper):
	a.)	Loop through every number "j" in the domain [i, upper):
		i.)	Compute the product of "i" and "j"
		ii.)	If the product is greator than the largest palindrome
			stored, validate that it is a palindrome - if it is,
			update the largest.

"""

digits	= 3
lower	= 10 ** (digits - 1)
upper	= 10 ** digits


def is_palindrome (n):
	backwards = 0
	temp = n
	
	while 0 < temp:
		digit = temp % 10
		temp /= 10
		
		backwards *= 10
		backwards += digit
	
	if n == backwards:
		return True
	
	return False


def largest_palindrome_product (a, b):
	largest = 0
	i = a
	while i < b:
		j = i
		while j < b:
			product = i * j
			if largest < product and is_palindrome(product):
				largest = product
			j += 1
		i += 1
	
	return largest


print largest_palindrome_product(lower, upper)


