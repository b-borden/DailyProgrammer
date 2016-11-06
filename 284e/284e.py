# The two 'if's to check beginning and end of dictionary words could be represented
# in the regex as '^' and '$', however they turn out to be quite effective at quick
# pruning of dictionary words that don't match the beginning an end of the sequence,
#  hitting the regex constantly, slowing down

import re

dictionary = set(line.strip() for line in open('enable1.txt'))


def swype_words(seq):
	for d in dictionary:
		if len(d) < 5:
			continue
		if d[0] != seq[0]:
			continue
		if d[-1] != seq[-1]:
			continue
		d_no_reps = re.sub(r'([a-z])\1', r'\1', d)
		if re.search('.*?'.join([l for l in d_no_reps]), seq):
			yield d


inputs = '''qwertyuytresdftyuioknn
gijakjthoijerjidsdfnokg'''

for seq in inputs.splitlines():
	print(list(swype_words(seq)))
