# Contador de Vogais e Consoantes
# Escreva um script que conte o número de vogais e consoantes em uma frase fornecida pelo usuário.

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

def contador_vogais_consoantes(frase_usuario):
    """ Esta função conta o número de vogais e consoantes de uma frase fornecida pelo usuário.

    Parâmetros: 
        frase_usuario: str
            frase fornecidada pelo usuario.
    
    Retorna:
        qtd_vogais: int
            quantidade de vogais

        qtd_consoante: int
            quantidade de consoantes
    """
    qtd_vogais = 0
    qtd_consoantes = 0
    for letra in frase_usuario:
        if letra in vogais:
            qtd_vogais += 1
        elif letra in consoantes:
            qtd_consoantes +=1
    return qtd_vogais, qtd_consoantes

frase_usuario = input("Digite uma frase (sem acento ou Ç): ").lower()
qtd_vogais, qtd_consoantes = contador_vogais_consoantes(frase_usuario)
print("Quantidade de vogais:", qtd_vogais)
print("Quantidade de consoantes:", qtd_consoantes)   