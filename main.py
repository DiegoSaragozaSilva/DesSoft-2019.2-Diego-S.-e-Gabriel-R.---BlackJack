#Imports para o código
import random

#Criação do baralho como uma lista 2D
Baralho = [0] * 13

#Dinheiro inicial do player
Dinheiro=100

#Atribuição de valores nas cartas do baralho
for i in range(0, len(Baralho)):
    if i == 0:
        Baralho[i] = 11
    elif i < 10:
        Baralho[i] = i + 1
    else:
        Baralho[i] = 10

Baralho *= 4
print(Baralho)
#Randomização do baralho
random.shuffle(Baralho)

def retornaCartas():
    for i in range(2):
        x = random.randint(0, len(Baralho) - 1)
        print(x)
        print(Baralho)
        a = Baralho[x]
        Baralho.pop(x)
    return a

#Loop de apostas
aposta = int(input("Digite o quato vai apostar:"))
while aposta < 1:
    print("aposta invalida")
    aposta = int(input("Digite o quato vai apostar:"))

while aposta >= 1:
    Dinheiro -= aposta
    a = retornaCartas()
