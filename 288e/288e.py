# This gives a different output than the challenge example output;
# It consistently applies a more complete stop word list

# Need to do nltk.download() to download stopword corpus before running this

import re
from nltk.corpus import stopwords
stop_set = set(stopwords.words('english'))

def remove_duplicates(_list):
	out = []
	for x in _list:
		if x not in out:
			out.append(x)
	return out

def alliteration(s):
	s = re.sub('[^A-Za-z_ ]', '', s)
	words_no_stops = [w for w in s.lower().split() if w not in stop_set]

	prev_word = '_'
	alliteration_words = []
	for word in words_no_stops:
		if word[0] == prev_word[0]:
			alliteration_words.extend([prev_word, word])
		prev_word = word
	return ' '.join(remove_duplicates(alliteration_words))


inputs = '''The daily diary of the American dream
For the sky and the sea, and the sea and the sky
Three grey geese in a green field grazing, Grey were the geese and green was the grazing.
But a better butter makes a batter better.
"His soul swooned slowly as he heard the snow falling faintly through the universe and faintly falling, like the descent of their last end, upon all the living and the dead."
Whisper words of wisdom, let it be.
They paved paradise and put up a parking lot.
So what we gonna have, dessert or disaster?'''

for s in inputs.splitlines():
	print(alliteration(s))
