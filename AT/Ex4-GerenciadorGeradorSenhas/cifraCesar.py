# Codificador/Decodificador de Mensagens de acordo com a Cifra de César
# Eu implementei este script no exercício 10 do TP3 e estou reaproveitando para a implementação do exercício 4 do AT.
# A única alteração realizada neste script foi permitir que letras minúsculas, maiúsculas, números, caracteres especiais e o espaço em branco sejam codificados e decodificados.

alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = alfabeto_minusculo.upper()
lista_numeros = "0123456789"
lista_caractere_especial = "@!#$&*-+=?.,:;_"
alfabeto_original = alfabeto_minusculo + alfabeto_maiusculo + lista_numeros + lista_caractere_especial + " "

def obtem_alfabeto_cifrado(deslocamento = 3):
    """
    Gera um alfabeto cujas letras estão deslocadas em relação ao alfabeto convencional.

    Parâmetros:
        - deslocamento: int (default: 3)
    
    Retorna:
        - alfabeto_cifra: str
            Alfabeto com deslocamento.
    """
    alfabeto_cifra = alfabeto_original[deslocamento:] + alfabeto_original[:deslocamento]
    return alfabeto_cifra

def decodifica(frase_codificada, deslocamento = 3):
    """
    Recupera a frase original a partir de uma frase codificada por um dado alfabeto cifrado.

    Parâmetros:
        - frase_codificada: str
            Frase gerada com o alfabeto cifrado
        - deslocamento: int (default: 3)
    
    Retorna:
        - frase_decodificada: str
    """
    alfabeto_cifra = obtem_alfabeto_cifrado(deslocamento)
    cifra_para_letra = {alfabeto_cifra[i]: alfabeto_original[i] for i in range(len(alfabeto_original))} 
    frase_decodificada = ""
    for letra in frase_codificada:
        if letra in cifra_para_letra:
            frase_decodificada += cifra_para_letra[letra]
    return frase_decodificada

def codifica(frase, deslocamento = 3):
    """
    Codifica a frase utilizando um alfabeto cifrado.

    Parâmetros:
        - frase: str
            Frase gera ser codificada.
        - deslocamento: int (default: 3)
    
    Retorna:
        - frase_codificada: str
    """
    alfabeto_cifra = obtem_alfabeto_cifrado(deslocamento)
    letra_para_cifra = {alfabeto_original[i]: alfabeto_cifra[i] for i in range(len(alfabeto_original))}

    frase_codificada = "" 
    for letra in frase:
        if letra in letra_para_cifra:
            frase_codificada += str(letra_para_cifra[letra]) 
    return frase_codificada