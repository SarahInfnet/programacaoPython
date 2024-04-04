#Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
import random
numero_secreto = random.randint(1,100)
max_tentativas = 5
ganhou = False
for i in range(max_tentativas):
    palpite_usuario = int(input("Tente adivinhar o numero secreto. Escolha um numero inteiro(1-100): "))
    if palpite_usuario == numero_secreto :
        ganhou = True
        break
    if palpite_usuario > numero_secreto :
        print("Palpite alto!")
    if palpite_usuario < numero_secreto :
        print("Palpite baixo!")
if ganhou == True:
    print("Palpite correto. Parabéns!")
else:
    print("Você errou todas as tentativas! O numero escolhido pelo computador foi",numero_secreto,".")