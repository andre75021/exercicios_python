largura = int(input("Digite a largura: "))

altura = int(input("Digite a altura: "))

if altura == 2:
    aux = altura -1
else:
    aux = altura - 2    
caractere = "#"

while altura > 0:
    if altura > 1:
        print(caractere * largura)
    while aux > 0:
        print(caractere + " " * (largura - 2) + caractere)
        aux -= 1
    altura -= 1


