fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except Exception as e:
    print("File can't be opened",fname)
    exit()

count = dict()
maior = None
for line in fhand:
    if not line.startswith('From'):
        continue
    words = line.split()
    if not words[1] in count:
        count[words[1]] = 1
    else:
        count[words[1]] += 1
    #print(words[1])

for keys in count:
    if maior == None:
        maior = keys
    else:
        if not count[keys] > count[maior]:
            continue
        else:
            maior = keys

print(maior.strip(),5)
print(len(count))
