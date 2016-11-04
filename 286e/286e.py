def reverse_fact(n):
	factor = 2
	if n == 1: return '0! and 1!'
	while n % factor == 0:
		if n == factor:
			return str(factor) + '!'
		n /= factor
		factor += 1
	return 'NONE'

print(reverse_fact(3628800))
print(reverse_fact(479001600))
print(reverse_fact(6))
print(reverse_fact(18))