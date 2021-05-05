"""tabela = {
    "Alface": 0.45,
    "Batata": 1.2,
    "Tomate": 2.3,
    "Feijao": 1.5}

    while True:
        produto = input("Digite o nome do produto(fim para terminar).: ")
        if produto == "fim":
            break
            if produto in tabela:
                print(f"Preço do produto: {tabela[produto]:5.2f}")
            else:
                print("Produto não encontrado"""

stuff = dict()
a = stuff.get('candy')
print(stuff.get('candy',-1))
print(a)
