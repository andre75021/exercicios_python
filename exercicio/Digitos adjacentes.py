n = int(input("Digite um número inteiro: "))

aux = 0
i = 0
count = 0
while n >= 1:
    i = n % 10
    n = n // 10
    aux = n % 10
    if i == aux:
        count = count + 1

if count > 0 :
    print("Sim")
else:
    print("Não")
