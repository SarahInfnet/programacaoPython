# Contador de Números Positivos
# Problema: Escreva um programa que utilize um loop for para percorrer uma lista de números gerados aleatoriamente e conte quantos são positivos. 
import random 

n = 50
a = -100
b = 100
lista_aleatoria = []
contador_positivos = 0
for i in range(n):
    numero_aleatorio = random.randint(a,b)
    if numero_aleatorio >= 0:
        contador_positivos += 1
    lista_aleatoria.append(numero_aleatorio)

print(lista_aleatoria)
print(f"A lista tem {contador_positivos} números positivos.")