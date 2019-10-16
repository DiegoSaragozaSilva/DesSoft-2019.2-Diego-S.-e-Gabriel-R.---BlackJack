#Imports para o código
import random

#Criação do baralho como uma lista
Baralho = [0] * 13
#Soma das cartas na mão da máquina

SomaPC = 0
#Variável que controla quando o jogador está jogando e apostando ou não
Jogando = True
Apostando = False
#Boas vindas!
print("Bem vindo à mesa de Black Jack! ")

#Input do jogador para determinar o numero de jogadores:
NJ=int(input("Quantos jogadores irao jogar?"))
#Dinheiro inicial Para cada jogador jogadores player:
Dinheiro=[]
for i in range(NJ):
    Dinheiro.append(100)
#Listas para o jogo
aposta=[0] * NJ
SomaJ=[0] * NJ

#Input do jogador para determinar o numero de baralhos:
NB = int(input("Quantos baralhos você deseja? "))

####
z = []
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
while Jogando:
    for i in range(len(Dinheiro)):
        #Recebimento da aposta
        print("Jogador {0} Seu dinheiro é U${1}".format(i+1,Dinheiro[i]))
        aposta[i] = float(input("Jogador {0} Digite o quanto vai apostar:".format(i+1)))

        #Verificação de aposta inválida
        if aposta[i] < 1 or aposta[i] > Dinheiro[i]:
            print("Jogador {0} Aposta invalida! Aposte valores maiores que 0!".format(i+1))
            aposta[i] = float(input("Jogador {0} Digite o quanto vai apostar:".format(i+1)))

        elif aposta[i] >= 1:
            Apostando = True
    for i in range(len(Dinheiro)):
        Apostando = True 
        SomaPC = 0
        while Apostando:
        
            #Loop de apostas
            Dinheiro[i] -= aposta[i]
            cartasJ = retornaCartas(2)
            SomaJ[i] = cartasJ[0] + cartasJ[1]
            print(Dinheiro[i])
            #Verificação de 2 A's
            if SomaJ[i] == 22:
                SomaJ[i] == 12

            #Verificação de Blackjack
            if SomaJ[i] == 21:
                print("Jogador {0} BLACKJACK! Você ganhou!".format(i+1))
                Dinheiro[i] = Dinheiro[i] + aposta[i] * 1.5
                SomaJ[i] = 0

            #Verificação de continuidade da aposta
            while Apostando:
                    print("Jogador {0} Você tem {1} pontos.".format(i+1, int(SomaJ[i])))
                    resp = input("Jogador {0} Deseja mais uma carta? Digite 'sim' ou 'não'".format(i+1))
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
        SomaPC+= float(cartasPC[0])
         #Validação do Ás como 11 ou 1
        if cartasPC[0] == 11 and cartasPC[0] + SomaPC > 21:
            cartasPC[0] = 1
            SomaPC += float(cartasPC[0])
        print(SomaPC)

    for i in range(len(Dinheiro)):
        #Verificação de derrota
        if SomaJ[i] > 21 or (SomaPC > SomaJ[i] and SomaPC < 21):
            print("Jogador {0} O dealer fez {1} e você fez {2}".format(i+1,SomaPC, SomaJ[i]))
            print("Você perdeu!")
            Dinheiro[i]= Dinheiro[i]-aposta[i]

        #Verificação de vitória        
        elif SomaPC < SomaJ[i] and SomaJ[i] <= 21 or (SomaPC > 21 and SomaJ[i] <= 21):
            print("Jogador {0} O dealer fez {1} e você fez {2}".format(i+1,SomaPC, SomaJ[i]))
            print("Você ganhou!")
            Dinheiro[i] += aposta[i] * 2
            SomaJ[i] = 0

        #Verificação de empate
        elif SomaJ[i] == SomaPC:
            print("Jogador {0} O dealer fez {1} e você fez {2}".format(i+1,SomaPC, SomaJ[i]))
            print("O jogo empatou!")
            Dinheiro[i] += aposta[i]
            SomaJ[i] = 0

    for i in range(len(Dinheiro)):
        resp = input("Jogador {0} deseja continuar jogando? Digite 'sim' ou 'não'".format(i+1))

        if resp == 'não':
            z.append(i)
        elif resp == 'não' and len(Dinheiro) == 1:
            Jogando=False
            Apostando=False
        elif resp == 'sim' and Dinheiro[i] > 0:
            Dinheiro[i] += aposta[i]
            SomaJ[i] = 0
            Apostando = False
        elif resp == 'sim' and Dinheiro[i] <= 0:
            print("Jogador {0} Você não tem mais dinheiro para apostar! Até a próxima!".format(i+1))
            z.append(i)
            Apostando = False
            if len(Dinheiro) == 1:
                Jogando = False
    
    for player in z:
        Dinheiro.pop(player)
        aposta.pop(player)
        SomaJ.pop(player)