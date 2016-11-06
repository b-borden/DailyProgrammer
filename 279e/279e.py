# Turns out that python has a built-in to do uuencoding. Just need to convert input into bytes
# and pad zeros at end if necessary to make bytes length a multiple of 3.

import codecs

def uuencode(msg):
	bytes = msg.encode()
	# Pad to an even multiple of 3 bytes with zeros
	bytes += b'0' * ((3 - (len(bytes) % 3)) % 3)
	uuencoded = codecs.encode(bytes, 'uu')

	return uuencoded.decode()

def uudecode(msg):
	return codecs.decode(msg.encode(), 'uu').decode()

uu1 = uuencode('Cat')
uu2 = uuencode('''I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life.''')
print(uu1)
print(uu2)

print('Bonus 1:')
print(uudecode(uu1))
print(uudecode(uu2))