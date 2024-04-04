#Problema: Implemente uma função que desenhe uma linha padrão na tela sem que sejam passados argumentos para a função, porém aceitando como parâmetros definidos por posição um caractere para construir a linha e o comprimento da linha

def criar_linha(caractere = "-", tamanho = 10):
    """ Esta função cria uma linha padrão.

    Parâmetros:
        - caractere: str
            String para formar a linha
    
        - tamanho: int
            Quantidade de caracteres para formar a linha.
    """
    print(caractere*tamanho)

print("Criando linha sem passar parâmetros: ")
criar_linha()
print("Criando linha personalizada pelo usuário: ")
quantidade_caracteres = int(input("Quantos caracteres vão ser utilizados pra formar a linha? "))
caracter = input("Escolha um caracter pra formar a linha? ")
criar_linha(caracter, quantidade_caracteres)