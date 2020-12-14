n = int(input("Digite um número inteiro: "))

i = n
count = 0
while i > 0:
    if n % i == 0:
        count = count + 1
    i = i -1

if count == 2:
    print("Primo")
else:
    print("Não primo")


          
    
