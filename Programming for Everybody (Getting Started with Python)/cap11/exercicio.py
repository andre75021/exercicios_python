
import re
def soma_numeros(lista):
	plus = 0
	for numero in lista:		
		num = int(numero)
		plus = plus + num
	return plus

hand = open('regex_sum_1099464.txt')
soma = 0
for line in hand:
	line = line.rstrip()
	if not re.findall('[0-9]+', line):
		continue
	l = re.findall('[0-9]+', line)
	#vf = soma_numeros(l)
	soma = soma + soma_numeros(l)
print(soma)