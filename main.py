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
Apostando = False

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
def retornaCartas(n):
    print(n)
    a = [0] * n
    for i in range(n):
        x = random.randint(0, len(Baralho) - 1)
        a[i] = Baralho.pop(x)
        print(len(Baralho))
    return a

#Loop principal
while Jogando and Dinheiro > 0:
    #Recebimento da aposta
    print("Seu dinheiro é U${0}".format(Dinheiro))
    aposta = int(input("Digite o quanto vai apostar:"))

    #Verificação de aposta inválida
    if aposta < 1 or aposta > Dinheiro:
        print("Aposta invalida! Aposte valores maiores que 0!")
        aposta = int(input("Digite o quanto vai apostar:"))

    elif aposta >= 1:
        Apostando = True
        
        while Apostando:
            #Loop de apostas
            Dinheiro -= aposta
            cartasJ = retornaCartas(2)
            print("Aqui chamou 1")
            SomaJ += cartasJ[0] + cartasJ[1]
            if not SomaPC >= 17:
                cartasPC = retornaCartas(2)
                print("Aqui chamou 2")
                SomaPC += cartasPC[0] + cartasPC[0]

            #Verificação de Blackjack
            if SomaJ == 21:
                print("BLACKJACK! Você ganhou!")
                Dinheiro += aposta * 1.5
            
            #Verificação de continuidade da aposta
            while Apostando:
                print("Você tem {0} pontos.".format(SomaJ))
                resp = input("Deseja mais uma carta? Digite 'sim' ou 'não'")
                if resp == 'não':
                    Apostando = False
                elif resp == 'sim':
                    cartasJ = retornaCartas(1)
                    print("Aqui chamou 3")
                    SomaJ += int(cartasJ[0])
                    if SomaJ > 21:
                        Apostando = False
                    if not SomaPC >= 17:
                        cartasPC = retornaCartas(1)
                        print("Aqui chamou 4")
                        SomaPC += int(cartasPC[0])
                    
    #Verificação de derrota
    if SomaJ > 21 or SomaPC > SomaJ and SomaPC <= 21:
        print("O dealer fez {0} e você fez {1}".format(SomaPC, SomaJ))
        resp = input("Você perdeu! Deseja continuar jogando? Digite 'sim' ou 'não'")

        if resp == 'não':
            Jogando = False
            Apostando = False
        elif resp == 'sim':
            SomaJ = 0
            SomaPC = 0
            Apostando = False
            
    #Verificação de vitória        
    elif SomaJ <= 21 and SomaPC < SomaJ:
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
