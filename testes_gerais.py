def minimo(lista):
    var_minimo = None
    print(f"Antes.: {var_minimo}")
    for intervar in lista:
        if (var_minimo == None) or intervar < var_minimo:
            var_minimo = intervar
        print(f"Laço.: {intervar} {var_minimo}")
    print(f"Mínimo.: {var_minimo}")



def maximo(lista):
    var_maximo = None
    print(f"Antes: {var_maximo}")
    for intervar in lista:
        if (var_maximo == None) or intervar > var_maximo:
            var_maximo = intervar
            print(f"Laço: {intervar} {var_maximo}")
    print(f"Máximo: {var_maximo}")

a = [3,41,12,9,74,15]

maximo(a)
print()
minimo(a)
