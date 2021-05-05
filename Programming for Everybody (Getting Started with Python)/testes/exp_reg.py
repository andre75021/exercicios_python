import re

def abrir():
	return open('mbox-short.txt')

def regular(hand):
	for line in hand:
		line = line.rstrip()
		if re.search('From: ', line):
			print(line)


def regular2(hand):
	for line in hand:
		line = line.rstrip()
		if re.search('^From:', line):
			print(line)

def regular3(hand):
	for line in hand:
		line = line.rstrip()
		if re.search('FROM.+uk', line):
			print(line)

#regular(abrir())
print('--------------------------------')	
#regular2(abrir())
regular3(abrir())

