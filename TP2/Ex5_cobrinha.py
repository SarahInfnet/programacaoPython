#Problema: Escreva um programa que utilize um loop for para gerar uma lista dos quadrados dos números de 1 a 20.

lista_quadrados = []
for i in range(1,21):
    quadrado = i **2
    lista_quadrados.append(quadrado)
    print(i, "ao quadrado é", quadrado)

print(lista_quadrados)