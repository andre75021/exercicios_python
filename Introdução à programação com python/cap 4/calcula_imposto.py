salario = float(input('Entre com a salario.: '))

base = salario
imposto = 0

if base > 3000:
	imposto = imposto + ((base - 3000) * 0.35)
	base = 3000
if base > 1000:
	imposto = imposto + ((base - 1000) * 0.2)

print('O valor de imposto à pagar é de.: {:5.2f}'.format (imposto))	
