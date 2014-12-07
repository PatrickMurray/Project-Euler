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
