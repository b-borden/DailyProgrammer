# Including bonus 1

def largest_digit(num):
	return max(str(num))

print(largest_digit(1234))
print(largest_digit(3253))
print(largest_digit(9800))
print(largest_digit(3333))
print(largest_digit(120))

# Bonus 1
def desc_digits(num):
	return ''.join(sorted('%04d' % num, reverse=True))

print('Bonus #1:')
print(desc_digits(1234))
print(desc_digits(3253))
print(desc_digits(9800))
print(desc_digits(3333))
print(desc_digits(120))