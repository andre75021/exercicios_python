print('1. Conversão para segundos')
print('2. Aumento de salário')
print('3. Total da venda')
print('4. Tempo de viagem')
print('5. Converte temperatura')
print('')

try:
    choice = input('Choice the exercice: ')

    if choice == '1' :
        print()
        print('========================xxxxxxxxxxxxxxx========================')
        print()
        dias = int(input("Entre com o número de dias: "))
        horas = int(input("Entre com a quantidade de horas: "))
        minutos = int(input("Entre com a quantidade de minutos: "))
        segundos = int(input("Entre com a quantidade de segundos: "))

        totSec = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

        print("A quantidade de segundos no tempo informado é de: {} sec".format (totSec))


    elif choice == '2':
        print()
        print('========================xxxxxxxxxxxxxxx========================')
        print()

        salario = float(input('Entre com o salário: '))
        taxa_reajuste = float(input('Entre com a taxa de reajuste: '))
        novo_salario = salario + (salario * (taxa_reajuste / 100))

        print("O novo salário será de: {:5.2f} reais".format (novo_salario))
    elif choice == '3' :
        print()
        print('========================xxxxxxxxxxxxxxx========================')
        print()

        pco_venda = float(input('Entre com o valor da mercadoria: '))
        qtd_venda = int(input('Entre com a quantidade a ser vendida: '))
        desconto = float(input('Desconto (em %): '))
        tot_venda = pco_venda * qtd_venda
        
        total_pagar = tot_venda - (tot_venda * (desconto / 100))

        print('Total à pagar é de: {:5.2f} R$'.format (total_pagar))
    elif choice == '4' :
        print()
        print('========================xxxxxxxxxxxxxxx========================')
        print()        

        distancia = int(input('Qual a distância da viagem (KM): '))
        velocidade = int(input('Qual a velocidade pretendida (KM/H): '))

        tempo_de_viagem = distancia / velocidade
        if tempo_de_viagem < 1:
            tempo_de_viagem = tempo_de_viagem * 60
            print('O tempo de viagem será de {:5.2f} mins'.format (tempo_de_viagem))
        else:
            print('O tempo de viagem será de {:5.2f} hrs'.format (tempo_de_viagem))

    elif choice == '5' :
        print()
        print('========================xxxxxxxxxxxxxxx========================')
        print()

        temp = float(input('Entre com a temperatura (ºC): '))

        temp_fah = ((9 * temp) / 5) + 32

        print('A temperatura em ºF é de {} ºF'.format (temp_fah))
    
    else:
        print('Entre com um número válido')

except:
    print('Deu merda')
