#Problema: Escreva um programa que verifique entre todos os números de 1 a 100 quais são números primos e exiba uma lista com todos

lista_num_primos = []

for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            lista_num_primos.append(num)

print(f"Números primos de 1 a 100: {lista_num_primos}")
