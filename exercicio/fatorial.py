n = int(input("Digite o nuúmero.: "))

resultado = 1
count = 1

if n == 0:
	print("1")
else:
	while count <= n:
		resultado *= count
		count += 1  
print (resultado)
