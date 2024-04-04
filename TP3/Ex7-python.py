# Gerador de Senha Aleatória
# Crie um programa que gere senhas aleatórias com letras (maiúsculas e minúsculas), números e símbolos, permitindo ao usuário especificar o comprimento da senha.

import random

alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = alfabeto_minusculo.upper()
lista_numeros = "0123456789"
lista_simbolos = "@!#$$&*-+=?"
lista_caracteres = alfabeto_maiusculo + alfabeto_minusculo + lista_numeros + lista_simbolos

def gerador_senha(tamanho = 8):
    """ Esta função gera uma senha aleatória.

    Parâmetros:
        - tamanho: int
            número que define qual irá ser o tamanho da senha.
    
    Retorno:
        - senha: str
            senha aleatória.
    """
    senha = ""
    for i in range(tamanho):
        senha += random.choice(lista_caracteres)
    return senha

tamanho = int(input("Qual o tamanho da senha? "))
print(gerador_senha(tamanho))