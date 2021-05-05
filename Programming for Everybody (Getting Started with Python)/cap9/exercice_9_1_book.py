fname = 'words.txt'
fh = open(fname)
count = 0
dicio = dict()
repete = dict()

for line in fh:
	for word in (line.split()):
		dicio[word] = count
		repete[word] = repete.get(word,0) + 1
		count += 1
#	print('OK')

for word in repete:
	print(word, repete[word])

