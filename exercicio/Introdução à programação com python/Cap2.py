# Calcula aumento

salario = float(input("Digite o salário: "))
perc = float(input("Digite o percentual de ajuste: "))

salario = (salario * (perc / 100)) + salario

print ("O novo salário será de: ", salario)
