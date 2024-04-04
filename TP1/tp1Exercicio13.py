#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
palavra_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
palavra_usuario_sem_espacos = palavra_usuario.replace(" ","").lower()
if palavra_usuario_sem_espacos == palavra_usuario_sem_espacos[::-1]:
    print(palavra_usuario, "é um palíndromo")
else:
    print(palavra_usuario, "não é um palíndromo")
