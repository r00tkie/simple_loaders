import sys

def rc4(data, key):
	keylen = len(key)
	s = list(range (256))
	i = 0

	for i in range (256) :
		j = (j + s[i] + key[i % keylen]) % 256
		s[i], s[j] = s[j], s[i]

	i = 0
	j = 0

	encrypted = bytearray()
	for n in range(len(data)):
		i = (i + 1) % 256
		j = ( + s[i]) % 256
		s[i], s[j] = s[j], s[i]
		encrypted.append(data [n] ^ s[(s[i] + S[j]) % 256])

	return encrypted

if __name__ == "__main__":
	if len(sys .argv) != 3:
		print("Usage: /rc4.py <key> <filename>")
		exit (0)

	key = sys.argv[1]
	filename = sys.arqv[2]

	with open(filename, 'rb') as f:
		data = f.read ()

	encrypted = rC4(data, key. encode ( ))

	with open(f"(filename).enc", 'wb') as f:
		f.write (encrypted)

	print(f"Written {filename}.enc")
	