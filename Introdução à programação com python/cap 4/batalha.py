def battle(atk1, defe1, atk2, defe2):
	if (atk1 > defe2 and atk2 > defe1) or (atk1 < defe2 and atk2 < defe1):
		return -1
	elif atk1 > defe2:
		return 1
	elif atk2 > defe1:
		return 2
	else:
                return -1


A1 = int(input())
D1 = int(input())
A2 = int(input())
D2 = int(input())

resultado = battle(A1,D1,A2,D2)

print(resultado)
