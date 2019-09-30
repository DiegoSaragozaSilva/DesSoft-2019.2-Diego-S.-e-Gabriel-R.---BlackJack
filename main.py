
#Criação do baralho como uma lista 2D
Baralho = [[0] * 13] * 4
#criacao da aposta inicial
ApostaInicial=100

#Atribuição de valores nas cartas do baralho
for i in range(4):
    for j in range(13):
        print(i, j)
        if j == 0:
            Baralho[i][j] = 11
        elif j < 10:
            Baralho[i][j] = j
        else:
            Baralho[i][j] = 10
aposta=int(input("Digite o quato vai apostar:"))
while a<1:
    print("aposta invalida")
    a=int(input("Digite o quato vai apostar:"))