#Problema: Escreva uma função que receba uma lista de números e imprima um histograma na tela (usando asteriscos para representar a frequência dos números). 
import random

def calculaFrequencia(lista_num):
    """ Esta função recebe uma lista de números e conta com que frequência aparecem.

    Parâmetros:
        - lista_num: list
            lista de números

    Retorna: 
        - frequencia: dict
            dicionário de frequencia
    """
    frequencia = {}
    for num in lista_num:
        if num in frequencia:
            frequencia[num] += 1 
        else:
            frequencia[num] = 1
    return frequencia

def exibeHistograma(lista_num, max_caracteres = 50):
    """ Esta função recebe uma lista de números e imprime um histograma.

    Parâmetros:
        - lista_num: list
            lista de números

        - max_caracteres: int
            quantidade de caracteres para criar o histograma
    """
    frequencia = calculaFrequencia(lista_num)
    numeros_ordenados = list(frequencia.keys())
    numeros_ordenados.sort()
    max_frequencia = max(frequencia.values())
    for numero in numeros_ordenados:
        tamanho_barra = int(frequencia[numero] / max_frequencia * max_caracteres)
        print(numero, "*" * tamanho_barra, f"({frequencia[numero]})")

a = 1
b = 10
quantidade_itens = int(input("Quantos itens deseja inserir na lista de numeros? "))
lista_num = []
for i in range(quantidade_itens):
    adicionar_num_lista = random.randint(a,b)
    lista_num.append(adicionar_num_lista)

calculaFrequencia(lista_num)
exibeHistograma(lista_num)

