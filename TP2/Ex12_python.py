#Problema: Desenvolva um programa que filtre uma lista de números, removendo aqueles que não satisfazem uma condição específica (por exemplo, ser par). 
lista_numeros = [1,2,3,4,5,6,7,8,9,10,40,67,33,87,80]
pares = []
for num in lista_numeros:
    if num % 2 == 0:
        pares.append(num)

lista_numeros = pares
print(lista_numeros)