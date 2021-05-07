"""Configuração de função com função."""


def imprime_lista(L, fimpressao, fcondicao):
    """Função ampla."""
    for i in L:
        if fcondicao(i):
            fimpressao(i)


def imprime_elemento(i):
    """Função que imprime o elemento."""
    print(f"Valor: {i}")


def epar(i):
    """Função que verifica se é par."""
    return i % 2 == 0


def eimpar(i):
    """Função que verifica se é impar."""
    return not epar(i)


dados = input('Entre com os dados (espaço entre os números): ').split()
dados = [int(s) for s in dados]
imprime_lista(dados, imprime_elemento, epar)
