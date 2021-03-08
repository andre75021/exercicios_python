fname = "romeo.txt"
fh = open(fname)

lista = list()

for linha in fh:
    linha.strip()
    line = linha.split()
    for palavra in line:
        if palavra in lista:
            continue
        lista.append(palavra)

lista.sort()

print(lista)
