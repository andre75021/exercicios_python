def detran(velocidade):
    multa = 5
    if velocidade > 80:
        excesso = velocidade - 80
        multa = excesso * multa
        return multa
    else:
        return 0

velocidade = int(input('Qual a velocidade do carro ? '))

resultado = detran(velocidade)

if resultado <= 0 :
    print('Parabéns, você é um motorista exemplar')
else:
    print('Você violou as leis de trânsito e precisa ser punido. Sua multa será.: {:5.2f} R$'.format(resultado))



