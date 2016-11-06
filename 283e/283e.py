import re

def find_anagram(inputs):
	l,r = inputs.replace('"', '').lower().split('?')
	if sorted(re.sub(r'\W', '', l)) == sorted(re.sub(r'\W', '', r)) and sorted(l.split()) != sorted(r.split()):
		return re.sub('\?', 'is an anagram of', inputs)
	else:
		return re.sub('\?', 'is NOT an anagram of', inputs)

inputs = '''"wisdom" ? "mid sow"
"Seth Rogan" ? "Gathers No"
"Reddit" ? "Eat Dirt"
"Schoolmaster" ? "The classroom"
"Astronomers" ? "Moon starer"
"Vacation Times" ? "I'm Not as Active"
"Dormitory" ? "Dirty Rooms"
"Just shuffled phrase" ? "Phrase just shuffled"'''

for line in inputs.splitlines():
	print(find_anagram(line))