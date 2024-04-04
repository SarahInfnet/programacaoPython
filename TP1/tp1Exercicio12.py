#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).
palavra_escolhida_usuario = input("Digite uma palavra: ")
quantidade_letras = len(palavra_escolhida_usuario)
if quantidade_letras < 5:
    print("A palavra escolhida tem", quantidade_letras, "letras.", "É uma palavra curta")
if quantidade_letras >= 5:
    print("A palavra escolhida tem", quantidade_letras, "letras.", "É uma palavra longa")
