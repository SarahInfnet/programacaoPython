#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
import random 
quantidade_dados = int(input("Digite quantos dados você deseja jogar? "))
for i in range(quantidade_dados):
    dado = random.randint(1,7)
    print("Você lançou", quantidade_dados, f"dados e o resultado do dado {i+1} foi: ", dado)
