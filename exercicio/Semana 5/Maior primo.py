def checa_primos(n):

    i = n
    count = 0
    count2 = 0
    while i > 0:
        if n % i == 0:
            count = count + 1
        i = i -1

    if count == 2:
        return True
    else:
        return False

def maior_primo(n):
    i = 0
    count = 0
    while i <= n:
        if checa_primos(i):
            count = i
        i = i + 1
    return count
    
