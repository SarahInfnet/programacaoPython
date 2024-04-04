#Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.
operação_escolhida_usuario = input("Escolha uma operação: (adicao/subtracao/multiplicacao/divisao) ")
primeiro_numero_escolhido_usuario = int(input("Escolha uma numero: "))
segundo_numero_escolhido_usuario = int(input("Escolha outro numero: "))

if operação_escolhida_usuario == "adicao":
    print("A soma de",primeiro_numero_escolhido_usuario, "e", segundo_numero_escolhido_usuario,"é",primeiro_numero_escolhido_usuario + segundo_numero_escolhido_usuario)
if operação_escolhida_usuario == "subtracao":
    print("A subtração de",primeiro_numero_escolhido_usuario, "e", segundo_numero_escolhido_usuario,"é",primeiro_numero_escolhido_usuario - segundo_numero_escolhido_usuario)
if operação_escolhida_usuario == "multiplicacao":
    print("A multiplicação de",primeiro_numero_escolhido_usuario, "e", segundo_numero_escolhido_usuario,"é",primeiro_numero_escolhido_usuario * segundo_numero_escolhido_usuario)
if operação_escolhida_usuario == "divisao":
    print("A divisão de",primeiro_numero_escolhido_usuario, "e", segundo_numero_escolhido_usuario,"é",primeiro_numero_escolhido_usuario / segundo_numero_escolhido_usuario)