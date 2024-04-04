#Problema: Crie um programa que simule o lançamento de um dado n vezes, armazenando os resultados em uma lista, depois calcule a média dos resultados e calcule a distribuição de frequência dos elementos da lista.
import random 
lista_lancamento_dados = []
quantidade_dados = int(input("Digite quantos dados você deseja jogar? "))
for i in range(quantidade_dados):
    dado = random.randint(1,6)
    lista_lancamento_dados.append(dado)

frequencia_elementos = {}
soma = 0   
for resultado in lista_lancamento_dados:
    soma += resultado
    if resultado in frequencia_elementos:
        frequencia_elementos[resultado] += 1
    else:
        frequencia_elementos[resultado] = 1

media = soma / quantidade_dados  

print("Lista de resultados armazenados:", lista_lancamento_dados)
print("Média:", media)
print("Frequência:", frequencia_elementos)
