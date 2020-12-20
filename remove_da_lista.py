def remove_repetidos(param):
    i = 0
    j = 0
    
    while i < (len(param)):

        while j < (len(param[:])):
            if param[i] == param[j]:
                param.remove(param[j])
            j += 1
        i += 1
    param.sort()
    return param 

lista = [7,3,33,12,3,3,3,7,12,100]
lista2 = [2, 3, 1, 1]


print(remove_repetidos(lista))
