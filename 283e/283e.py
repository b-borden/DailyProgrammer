import re

def find_anagram(inputs):
	phrases = inputs.lower().split('?')
	if sorted(re.sub(r'\W', '', phrases[0])) == sorted(re.sub(r'\W', '', phrases[1])):
		return re.sub('\?', 'is an anagram of', inputs)
	else:
		return re.sub('\?', 'is NOT an anagram of', inputs)

inputs = '''"wisdom" ? "mid sow"
"Seth Rogan" ? "Gathers No"
"Reddit" ? "Eat Dirt"
"Schoolmaster" ? "The classroom"
"Astronomers" ? "Moon starer"
"Vacation Times" ? "I'm Not as Active"
"Dormitory" ? "Dirty Rooms"'''

for line in inputs.splitlines():
	print(find_anagram(line))