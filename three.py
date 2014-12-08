"""

Largest Prime Factor
--------------------
Problem 3

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?


Approach (divide and conquer)
-----------------------------
As divisible primes are found, the number can be broken down.

Let:
	n = 600851475143

Steps:
1.)	Google & read up on prime numbers.
2.)	Keep track of the smallest prime number divisible by "n", initially
	the smallest prime number, two.
3.)	Loop:
	a.)	If the number and the smallest prime are divisible, divide the
		number by the prime and reset the largest prime back to its
		initial state.
	b.)	Otherwise, increase the largest prime number by one.

"""

n = 600851475143


def largest_prime(n):
	largest = 2
	while largest < n:
		if n % largest == 0:
			n /= largest
			largest = 2
		else:
			largest += 1
	
	return largest


print largest_prime(n)
