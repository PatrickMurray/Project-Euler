"""

Multiples of 3 and 5
--------------------
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Approach
--------
Let:
	a = 3
	b = 5
	limit = 1000

Steps:
1.)	Keep adding "a" while the sum is less than the limit.
2.)	Repeat step 1 for "b".
3.)	In steps 1 and 2, the common multiples that "a" and "b" share have
	been accounted for twice. Repeat step 1 with the product of "a" and
	"b" and subtract the result.

"""

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


result =  add_to_limit(a, limit)
result += add_to_limit(b, limit)
result -= add_to_limit(a * b, limit)

print result
