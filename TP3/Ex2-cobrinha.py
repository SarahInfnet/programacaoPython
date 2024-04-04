# Analisador de Frequência de Letras
# Escreva um programa que analise a frequência de cada letra em um texto e retorne um histograma dessa frequência.

def calculaFrequencia(frase):
    """ Esta função recebe uma sting e conta com que frequência aparecem os caracteres, sem fazer distinção entre caracteres maiúsculos e minúsculos. Espaços são removidos antes do cálculo das frêquencias ser realizado. Caracteres acentuados são tratados como caracteres distintos de suas versões não acentuadas.

    Parâmetros:
        - frase: str
            frase dada pelo usuario

    Retorna: 
        - frequencia: dict
            dicionário de frequencia
    """
    frase = frase.lower().replace(" ", "")
    frequencia = {}
    for letra in frase:
        if letra in frequencia:
            frequencia[letra] += 1 
        else:
            frequencia[letra] = 1
    return frequencia

def exibeHistogramaFrase(frase, max_caracteres = 50):
    """ Esta função recebe uma string e imprime um histograma.

    Parâmetros:
        - frase: str
            frase dada pelo usuario

        - max_caracteres: int
            quantidade de caracteres para criar o histograma
    """
    frequencia = calculaFrequencia(frase)
    caracteres_ordenados = list(frequencia.keys())
    caracteres_ordenados.sort()
    max_frequencia = max(frequencia.values())
    for caractere in caracteres_ordenados:
        tamanho_barra = int(frequencia[caractere] / max_frequencia * max_caracteres)
        print(caractere, "*" * tamanho_barra, f"({frequencia[caractere]})")

frase = input("Digite uma frase sem acentos: ")
exibeHistogramaFrase(frase)

