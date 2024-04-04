#Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
peso_usuario = float(input("Informe seu peso: "))
altura_usuario = float(input("Informe sua altura: (utilize ponto. ex: 1.58) "))
calculo_imc = peso_usuario / (altura_usuario * altura_usuario)
print(f"Seu IMC foi de {calculo_imc:.2f}")
if calculo_imc <= 18.5 :
    print("Abaixo do peso")
if calculo_imc > 18.5 and calculo_imc < 24.9 :
    print("Peso normal")
if calculo_imc >= 25.0 :
    print("Sobrepeso")