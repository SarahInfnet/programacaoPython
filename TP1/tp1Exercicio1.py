#Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.
primeiro_numero = float(input("Insira um número: "))
segundo_numero = float(input("Insira outro número: "))
soma_numeros = primeiro_numero + segundo_numero
subtracao_numeros = primeiro_numero - segundo_numero
multiplicacao_numeros = primeiro_numero * segundo_numero
divisao_numeros = primeiro_numero / segundo_numero
divisao_inteira = primeiro_numero // segundo_numero
print("Numeros escolhidos:", primeiro_numero, "e", segundo_numero)
print("Soma:", soma_numeros)
print("Subtração:", subtracao_numeros)
print("Multiplicação:", multiplicacao_numeros)
print("Divisão:", divisao_numeros)
print("Divisão inteira:", divisao_inteira)