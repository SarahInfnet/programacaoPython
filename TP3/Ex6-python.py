# Contador e classificador de caracteres
# Escreva um programa que receba uma string do usuário e retorne o número total de caracteres, de letras maiúsculas, letras minúsculas, números, caracteres especiais e barras de espaço desta string.
letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letrasMinusculas= letrasMaiusculas.lower()
num = "0123456789"
caracteres_especiais = "!@#$%&*()_-+=.;:,/?|'"
barras_espaco = " "

def calcula_estatisticas_frase(frase_usuario):
    """Extrai estatísticas básicas de uma frase, incluindo o número total de caracteres, de letras maiúsculas, letras minúsculas, números, caracteres especiais e barras de espaço.

    Parâmetros:
        - frase_usuario: str
            A frase sobre a qual serão extraídas estatísticas.

    Retorna:
        - qtd_caracteres: int
            A quantidade de caracteres.
        - qtd_maiuscula: int
            A quantidade de caracteres maiúsculos.
        - qtd_minuscula: int
            A quantidade de caracteres minúsculos.
        - qtd_num: int
            A quantidade de números.
        - qtd_caracteres_especiais: int
            A quantidade de caracteres especiais.
        - qtd_barras_espaco: int
            A quantidade de espaços em branco.
    """
    qtd_caracteres = len(frase_usuario)
    qtd_maiuscula = 0
    qtd_minuscula = 0
    qtd_num = 0
    qtd_caracteres_especiais = 0
    qtd_barras_espaco = 0
    for letra in frase_usuario:
        if letra in letrasMaiusculas:
            qtd_maiuscula += 1
        elif letra in letrasMinusculas:
            qtd_minuscula += 1
        elif letra in num:
            qtd_num += 1
        elif letra in caracteres_especiais:
            qtd_caracteres_especiais += 1
        elif letra in barras_espaco:
            qtd_barras_espaco +=1

    return qtd_caracteres, qtd_maiuscula, qtd_minuscula, qtd_num, qtd_caracteres_especiais, qtd_barras_espaco

frase_usuario = input("Digite algo (sem acentos): ")
estatisticas = calcula_estatisticas_frase(frase_usuario)
qtd_caracteres = estatisticas[0]
qtd_maiuscula = estatisticas[1]
qtd_minuscula = estatisticas[2]
qtd_num = estatisticas[3]
qtd_caracteres_especiais = estatisticas[4]
qtd_barras_espaco = estatisticas[5]
print("Quantidade de caracteres:", qtd_caracteres)
print("Quantidade de letras Maiúsculas:", qtd_maiuscula)
print("Quantidade de letras Minúsculas:", qtd_minuscula) 
print("Quantidade de números:", qtd_num) 
print("Quantidade de caracteres especiais:", qtd_caracteres_especiais) 
print("Quantidade de barras de espaço:", qtd_barras_espaco) 