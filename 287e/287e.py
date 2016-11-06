# Including bonus 1

# I was originally thinking that the search in bonus #2 may
# require some sort of memoization, but it runs very quickly
# here without any further optimization!

def largest_digit(num):
	return max(str(num))


print(largest_digit(1234))
print(largest_digit(3253))
print(largest_digit(9800))
print(largest_digit(3333))
print(largest_digit(120))


# Bonus 1
def desc_digits(num):
	return int(''.join(sorted('%04d' % num, reverse=True)))


print('Bonus #1:')
print(desc_digits(1234))
print(desc_digits(3253))
print(desc_digits(9800))
print(desc_digits(3333))
print(desc_digits(120))


# Bonus 2
def asc_digits(num):
	return int(''.join(str(desc_digits(num))[::-1]))


def kaprekar(num):
	i = 0
	while num != 6174:
		num = desc_digits(num) - asc_digits(num)
		i += 1
	return i


max_kaprekar = 0
for n in range(1, 10000):
	if len(set(str(n))) < 2:
		continue
	max_kaprekar = max(max_kaprekar, kaprekar(n))

print('Bonus #2:')
print("The largest number of iterations for Kaprekar's Routine is:", max_kaprekar)
