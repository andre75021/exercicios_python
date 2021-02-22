from functions import cria_lista
try:
    tamanho = int(input('Qual o tamanho da lista? '))
except:
    print('Entrada inválida!')

lista = cria_lista(tamanho)

print(lista)
