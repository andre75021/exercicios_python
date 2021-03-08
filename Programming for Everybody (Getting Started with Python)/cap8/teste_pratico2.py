fname = "mbox-short.txt"
fh = open(fname)
count =  0
for linha in fh:
    if not linha.startswith("From: "):
        continue
    lista = linha.split()
    print(lista[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
