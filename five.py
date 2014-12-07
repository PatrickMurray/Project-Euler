start	= 1
end		= 20


def least_common_multiple (a, b):
	return a * b / greatest_common_divisor(a, b)


def greatest_common_divisor (a, b):
	while 0 < b:
		temp = b
		b = a % b
		a = temp
	return a


result = start+1
for i in range(start, end+1):
	result = least_common_multiple(i, result)
	
print result
