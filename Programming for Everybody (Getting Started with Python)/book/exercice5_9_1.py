sumar = 0
while True:
    number = input("Number.: ")
    if (number == "pronto"):
        break
    try:
        number = int(number)
    except Exception as e:
        print("Algo Deu errado")
        continue
    sumar = sumar + number
print(sumar)
