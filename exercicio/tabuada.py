def mult():
    linha = 1
    coluna = 1
    while linha <= 10:
        while coluna <= 10:
            print(linha * coluna, end = '\t')
            coluna += 1
        print()
        linha += 1
        coluna = 1     

def div():
    linha = 1
    coluna = 1

    while linha <= 10:
        while coluna <= 10:
            result = (linha * 10) / coluna
            print ("{0:2.2f}".format(result), end = '\t')
            coluna += 1
        print()
        linha += 1
        coluna = 1


def somar():
    linha = 1
    coluna = 1

    while linha <= 10:
        while coluna <= 10:
            print(linha + coluna, end = '\t')
            coluna += 1
        print()
        linha += 1
        coluna = 1
   
mult()

print(' ')

somar()
