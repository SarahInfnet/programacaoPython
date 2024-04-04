#GeradorSenha
#Eu implementei este script no exercício 7 do TP3 e estou reaproveitando para a implementação do exercício 4 do AT.
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