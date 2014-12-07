digits = 3


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
	x = a
	while x < b:
		y = x
		while y < b:
			product = x * y
			if largest < product and is_palindrome(product):
				largest = product
			y += 1
		x += 1
	
	return largest


minimum = 10 ** (digits - 1)
maximum = 10 ** digits

print largest_palindrome_product(minimum, maximum)


