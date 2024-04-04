#Problema: Implemente um programa que organize uma lista de palavras em ordem crescente de tamanho.
lista_palavras = ["oi", "seja bem-vindo", "olá", "tchau"]
def organizar_palavras():
    """ Esta função organiza uma lista de palavras em ordem crescente de tamanho.
    """
    lista_palavras.sort(key = len)
    print(lista_palavras)

organizar_palavras()