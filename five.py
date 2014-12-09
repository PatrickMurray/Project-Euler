"""

Smallest Multiple
-----------------
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the
numbers from 1 to 20?


Approach
--------
Let:
	lower	= 1
	upper	= 20

Steps:
1.) Find the least common multiple of the lower number and the next
	number.
2.)	For the domain (lower, upper], find the least common multiple of
	each natural number and the result - updating the result each
	iteration.

"""

lower	= 1
upper	= 20


def least_common_multiple (a, b):
	return a * b / greatest_common_divisor(a, b)


def greatest_common_divisor (a, b):
	while 0 < b:
		temp = b
		b = a % b
		a = temp
	
	return a


result = upper + 1
i = lower
while i <= upper:
	result = least_common_multiple(i, result)
	i += 1
	
print result
