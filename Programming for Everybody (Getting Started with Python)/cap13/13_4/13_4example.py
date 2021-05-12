"""Exemplo de analise de Json."""
import json

dados = '''[
    {
        "id": "001",
        "x" : "2",
        "name" : "André"
    },
    {
        "id": "002",
        "x": "3",
        "name": "Luiz"
    },
    {
        "id": "003",
        "x": "4",
        "name": "Rodrigues"
    }
]'''

informacoes = json.loads(dados)
for itens in informacoes:
    print('Id: ', itens['id'])
    print('Nome: ', itens['name'])
    print('Atributo: ', itens['x'])
    print('====================================')
    print()
print('Nrº de usuários: ', len(informacoes))
