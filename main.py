#Imports para o código
import random

#Criação do baralho como uma lista
Baralho = [0] * 13
#Dinheiro inicial do player
Dinheiro=100
#Soma das cartas na mão do jogador e da máquina
SomaJ = 0
SomaPC = 0
#Variável que controla quando o jogador está jogando e apostando ou não
Jogando = True
Apostando = True

#Atribuição de valores nas cartas do baralho
for i in range(0, len(Baralho)):
    if i == 0:
        Baralho[i] = 11
    elif i < 10:
        Baralho[i] = i + 1
    else:
        Baralho[i] = 10

Baralho *= 4

#Randomização do baralho
random.shuffle(Baralho)

#Função que retorna o valor de duas cartas
def retornaCartas():
    a = [0] * 2
    for i in range(2):
        x = random.randint(0, len(Baralho) - 1)
        a[i] = Baralho.pop(x)
    return a

#Loop principal
while Jogando:
    #Recebimento da aposta
    print("Seu dinheiro é U${0}".format(Dinheiro))
    aposta = int(input("Digite o quanto vai apostar:"))


    #Verificação de aposta inválida
    if aposta < 1:
        print("Aposta invalida! Aposte valores maiores que 0!")
        aposta = int(input("Digite o quanto vai apostar:"))

    else:
        while Apostando:
            #Loop de apostas
            Dinheiro -= aposta
            cartasJ = retornaCartas()
            SomaJ += cartasJ[0] + cartasJ[1]
            cartasPC = retornaCartas()
            SomaPC += cartasPC[0] + cartasPC[1]

            #Verificação de Blackjack
            if SomaJ == 21:
                print("BLACKJACK! Você ganhou!")
                Dinheiro += Dinheiro * 1.5
            
            #Verificação de continuidade da aposta
            elif SomaJ < 21:
                print("Você tem {0} pontos.".format(SomaJ))
                resp = input("Deseja mais duas cartas? Digite 'sim' ou 'não'")
                if resp == "não":
                    Apostando = False
            
            #Verificação de derrota
            elif SomaJ > 21:
                resp = input("Você perdeu! Deseja continuar jogando? Digite 'sim' ou 'não'")
                if resp == 'não':
                    Jogando = False
                    Apostando = False
                    
