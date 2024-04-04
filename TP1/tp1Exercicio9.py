#Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.
valor_da_compra = float(input("Qual o valor da compra? "))
desconto_compra = 0
novo_valor = 0
if valor_da_compra > 200:
    desconto_compra = 0.15 * valor_da_compra
    novo_valor = valor_da_compra - desconto_compra
    print(f"O preço com desconto de 15% é: R$ {novo_valor:.2f}")
elif valor_da_compra > 100:
    desconto_compra = 0.1 * valor_da_compra
    novo_valor = valor_da_compra - desconto_compra
    print(f"O preço com desconto de 10% é: R$ {novo_valor:.2f}")
else:
    print("Não há desconto nesta compra. O valor da sua compra é de", valor_da_compra, "R$")
