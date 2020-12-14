def main():
	def_game = 0
	#Enquanto o usuário não entrar com um valor válido	
	while def_game == 0:
		# Opções de jogo
		print("Bem vindo ao jogo do NIM! Escolha:")
		print(" ")
		def_game = print("1- Para jogar uma partida isolada ")
		def_game = print("2- Para jogar um campeonato")
		# Solicita o tipo de jogo
	def_game = int(input(" "))
	if def_game == 1:
		print("Você escolheu uma partida isolada!")
		partida()
	#	break
	elif def_game == 2:
		print("Você escolheu um campeonato")
		campeonato()
	#	break
	else:
		print("Opção inválida")
		def_game = 0

def partida():

    print(" ")

    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True

    # Decide quem iniciará o jogo:
    if n % (m+1) == 0: is_computer_turn = False

    # Execute enquanto houver peças no jogo:
    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))

        # Retira as peças do jogo:
        n = n - jogada

        # Mostra o estado atual do jogo:
        print("Restam apenas {} peças em jogo.\n".format(n))

    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def usuario_escolhe_jogada(n, m):

    # Vez do usuário:
    print("Sua vez!\n")

    # Define o número de peças do usuário:
    jogada = 0

    # Enquanto o número não for válido
    while jogada == 0:

        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("Quantas peças irá tirar? "))

        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:

            # Valor inválido, continue solicitando ao usuário:
            jogada = 0

    # Número de peças válido, então retorne-o:
    return jogada

# Função de jogada do computador
def computador_escolhe_jogada(n,m):
	if n <= m:
		return n
	else:
		# Verifica melhor jogada
		mJogada = n % (m + 1)
		if mJogada > 0:
			return mJogada
		return m

# Função campeonato
def campeonato():
	#Pontuação de cada jogador
	usuario = 0 
	computador = 0
	nPartida = 1

	for _ in range(3):
		vencedor = partida()
		if vencedor == 1:
			usuario = usuario + 1
		else:
			computador = computador + 1



	# Placar final
	print(" ")
	print("**** Final do campeonato! ****")
	print(" ")
	print("Placar: Você {} X {} Computador".format(usuario, computador)) 



main()		
