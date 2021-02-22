def maior(x,y,z):
	if x > y and x > z:
		return x
	elif y > x and y > z:
		return y
	elif z > x and  z > y:
		return z



M = int(input())
A = int(input())
B = int(input())

C = (M - A - B)

resultado = maior(A,B,C)

print(resultado)

