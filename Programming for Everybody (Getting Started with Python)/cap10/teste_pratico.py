fhand = open('mbox-short.txt')
count = 0
dicio = dict()
for lines in fhand:
    if not lines.startswith('From '):
        continue
    line = lines.rstrip()
    line = line.split()
    hrs = line[5]
    hrs = hrs[:2]
    dicio[hrs] = dicio.get(hrs,0) + 1
    #print(hrs)
lista = list(dicio.items())
lista.sort()

for key, values in lista:
    print(key, values)
