def convert(n):

    expo = len(n) - 1
    i = 0
    termo = 0
    base = 0

    while expo >= 0:
        termo = (int(n[i])) *(2 ** expo)
        base = base + termo

        i += 1
        expo -= 1

    return base

def soma(a,b):
    return a + b


#n = input('Digite um número binário.: ')
#print(convert(n))

