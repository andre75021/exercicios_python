import re
#hand = open('mbox-short.txt')
hand = open('sped.txt')

lista = list()

for line in hand:
    line = line.rstrip()
    if re.findall('^|.+0',line):
        print(line)
