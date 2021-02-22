import random
def cria_lista(tamanho):
    lista = []
    for i in range(tamanho):
        x = random.randint(1,10000000000)
        lista.append(x)
    return lista
