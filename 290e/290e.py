def kaprekar(start, stop):
	for n in range(start, stop + 1):
		sqd = str(n ** 2)
		for i in range(1, len(sqd)):
			l = int(sqd[:i])
			r = int(sqd[i:])
			if r != 0 and l + r == n:
				yield n


print(list(kaprekar(1, 9000)))
