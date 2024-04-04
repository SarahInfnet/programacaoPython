#Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.
import random
primeiro_nome = input("Digite um nome: ")
segundo_nome = input("Digite outro nome: ")
ponto_divisao_primeiro_nome = random.randint(1,len(primeiro_nome))
primeiro_nome_dividido = [primeiro_nome[:ponto_divisao_primeiro_nome], primeiro_nome[ponto_divisao_primeiro_nome:]]
ponto_divisao_segundo_nome = random.randint(1, len(segundo_nome))
segundo_nome_dividido = [segundo_nome[:ponto_divisao_segundo_nome], segundo_nome[ponto_divisao_segundo_nome:]]
print("Aqui estão algumas possíveis combinações: ")
print(primeiro_nome_dividido[0] + segundo_nome_dividido[0])
print(primeiro_nome_dividido[0] + segundo_nome_dividido[1])
print(primeiro_nome_dividido[1] + segundo_nome_dividido[0])
print(primeiro_nome_dividido[1] + segundo_nome_dividido[1])
print(segundo_nome_dividido[0] + primeiro_nome_dividido[0])
print(segundo_nome_dividido[0] + primeiro_nome_dividido[1])
print(segundo_nome_dividido[1] + primeiro_nome_dividido[0])
print(segundo_nome_dividido[1] + primeiro_nome_dividido[1])