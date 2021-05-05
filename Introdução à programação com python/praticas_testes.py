# Abrindo um arquivo
fhand = open('mbox.txt')
print(fhand) #imprime o identificador de arquivo para acessar seu conteúdo

# ---- Lendo o arquivo -------
count = 0
lista = list()
for lines in fhand:
    count += 1
    line = lines.rstrip() # Retira os espaços em branco à direita
    if not line.startswith('From:'): # filtra as linhas por um prefixo
        continue # pula linhas que não me interessam
    if line.find('@uct.ac.za') == -1: # filtra algo na linha
        continue
    if line in lista:
        continue
    else:
        lista.append(line)
    print(lista)

print('Line count',count)

# a função fhand.open() carrega o arquivo para a  memória
