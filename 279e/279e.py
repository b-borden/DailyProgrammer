# Turns out that python has a built-in to do uuencoding. Just need to convert input into bytes,
# pad zeros at end if necessary to make bytes length a multiple of 3.  Lastly, chunk input into 45 byte groups
# to workaround a 45-byte max limitation of the built-in uuencode limitation

import binascii

def chunk(e, _size):
	for i in range(0, len(e), _size):
		yield e[i:i+_size]

def uuencode(msg):
	bytes = str.encode(msg)
	# Pad to an even multiple of 3 bytes with zeros
	bytes += b'0' * ((3 - (len(bytes) % 3)) % 3)
	uuencoded = ''.join([binascii.b2a_uu(byte_chunk).decode() for byte_chunk in chunk(bytes, 45)])

	return uuencoded.strip()

def uudecode(msg):
	for line in msg.splitlines():
		pass

uu1 = uuencode('Cat')
uu2 = uuencode('''I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life.''')
print('begin 644 cat.txt')
print(uu1)
print('`')
print('begin 644 text.txt')
print(uu2)
print('`')

print('Bonus 1:')
print(uudecode(uu1))
print(uudecode(uu2))