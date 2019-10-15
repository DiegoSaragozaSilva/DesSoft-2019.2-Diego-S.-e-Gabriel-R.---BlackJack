#Imports para o código
import random
#Criação do baralho como uma lista
Baralho = [0] * 13
#Soma das cartas na mão do jogador e da máquina
SomaJ = 0
SomaPC = 0
#Lista de futuras apostas:
Apostas=[]
#Lista da soma das cartas dos jogadores:
SomaJ=[]
#Variável que controla quando o jogador está jogando e apostando ou não
Jogando = True
Apostando = False

#Boas vindas!
print("Bem vindo à mesa de Black Jack! ")

#Input do jogador para determinar o numero de baralhos:
NB = int(input("Quantos baralhos você deseja? "))

#Input do jogador para determinar o numero de jogadores:
NJ=int(input("Quantos jogadores irão participar"))

#Dinheiro inicial Para cada jogador jogadores player:
Dinheiro=[]
for i in range(NJ):
    Dinheiro.append(100)
print(Dinheiro)
#Atribuição de valores nas cartas do baralho
for i in range(0, len(Baralho)):
    if i == 0:
        Baralho[i] = 11
    elif i < 10:
        Baralho[i] = i + 1
    else:
        Baralho[i] = 10

Baralho *= (4*NB)

#Randomização do baralho
random.shuffle(Baralho)

#Função que retorna o valor de duas cartas
def retornaCartas(n):
    a = [0] * n
    for i in range(n):
        x = random.randint(0, len(Baralho) - 1)
        a[i] = Baralho.pop(x)
    return a

#Loop principal
for i in range(len(Dinheiro)):
    while Jogando and Dinheiro[i] > 0:
        #Recebimento da aposta
        for i in range(1,NJ+1):
            print("Jogador numero {0}, Seu dinheiro é U${1}".format(i,Dinheiro[i-1]))
            aposta = int(input("Digite o quanto vai apostar:"))
        for i in range(len(Dinheiro)):
            #Verificação de aposta inválida
            if Apostas[i] < 1 or Apostas[i] > Dinheiro[i]:
                print("Aposta invalida! Aposte valores maiores que 0!")
                aposta = int(input("Digite o quanto vai apostar:"))
<<<<<<< HEAD

<<<<<<< HEAD
    elif aposta >= 1:
        Apostando = True
        
        while Apostando:
            #Loop de apostas
            Dinheiro -= aposta
            cartasJ = retornaCartas(2)
            SomaJ += cartasJ[0] + cartasJ[1]
            if not SomaPC >= 17:
                cartasPC = retornaCartas(2)
                SomaPC += cartasPC[0] + cartasPC[1]

            #Verificação de Blackjack
            if SomaJ == 21:
                print("BLACKJACK! Você ganhou!")
                Dinheiro += aposta * 1.5
                Apostando = False
            
            #Verificação de continuidade da aposta
=======
            elif Apostas[i] >= 1:
                Apostando = True
        for i in range(len(Dinheiro)):   
>>>>>>> ecfe43d9b37b13b7baab951d307ca7453ecf5458
=======

            elif Apostas[i] >= 1:
                Apostando = True
        for i in range(len(Dinheiro)):   
>>>>>>> ecfe43d9b37b13b7baab951d307ca7453ecf5458
            while Apostando:
                #Loop de apostas
                Dinheiro[i] -= Apostas[i]
                SomaJ[i] += retornaCartas(1) + retornaCartas(1)
                if not SomaPC >= 17:
                    cartasPC = retornaCartas(2)
                    SomaPC += cartasPC[0] + cartasPC[1]

                #Verificação de Blackjack
                if SomaJ[i] == 21:
                    print("Parabens jogador {0},BLACKJACK! Você ganhou!".format(i+1))
                    Dinheiro[i] += Apostas[i] * 1.5
                    Apostando == False
                
                #Verificação de continuidade da aposta
                while Apostando:
                    print("Jogador numero {0},Você tem {1} pontos.".format(i+1,SomaJ[i]))
                    resp = input("Deseja mais uma carta? Digite 'sim' ou 'não'")
                    if resp == 'não':
                        Apostando = False
                    elif resp == 'sim':
                        cartasJ = retornaCartas(1)
                        #Validação do Ás como 11 ou 1
                        if cartasJ[0] == 11 and cartasJ[0] + SomaJ[i] > 21:
                            cartasJ[0] = 1
                        SomaJ[i] += int(cartasJ[0])
                        if SomaJ[i] > 21 or SomaJ[i] == 21:
                            Apostando = False
    #Criação da mão do dealer
    while SomaPC<=17:
        cartasPC=retornaCartas(1)
        SomaPC+= int(cartasPC[0])
        #Validação do Ás como 11 ou 1
        if cartasPC[0] == 11 and cartasPC[0] + SomaPC > 21:
            cartasPC[0] = 1
            SomaPC += int(cartasPC[0])


    #Verificação de derrota
    if SomaJ > 21 or (SomaPC > SomaJ and SomaPC <= 21):
        print("O dealer fez {0} e você fez {1}".format(SomaPC, SomaJ))
        resp= input("Você perdeu! Deseja continuar jogando? Digite 'sim' ou 'não'")
        if resp == 'não':
            Jogando = False
            Apostando = False
        elif resp == 'sim':
            if Dinheiro == 0:
                print("Você não tem mais dinheiro para apostar! Até a próxima!")
                Apostando = False
                Jogando = False
            else:        
                SomaJ = 0
                SomaPC = 0
                Jogando = True
                Apostando = False

    #Verificação de vitória        
    elif (SomaJ <= 21 and SomaPC < SomaJ) or (SomaPC > 21 and SomaJ < 21):
        print("O dealer fez {0} e você fez {1}".format(SomaPC, SomaJ))
        resp = input("Você ganhou! Deseja continuar jogando? Digite 'sim' ou 'não'")
        
        if resp == 'não':
            Jogando = False
            Apostando = False
        elif resp == 'sim':
            Dinheiro += aposta * 2
            SomaJ = 0
            SomaPC = 0
            Apostando = False

    #Verificação de empate
    elif SomaJ == SomaPC:
        print("O dealer fez {0} e você fez {1}".format(SomaPC, SomaJ))
        resp = input("O jogo empatou! Deseja continuar jogando? Digite 'sim' ou 'não'")

        if resp == 'não':
            Jogando = False
            Apostando = False
        elif resp == 'sim':
            Dinheiro += aposta
            SomaJ = 0
            SomaPC = 0
            Apostando = False