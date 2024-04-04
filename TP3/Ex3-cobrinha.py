# Calculadora de Média com Suporte a Diferentes Separadores Decimais
# Crie um programa que solicite ao usuário uma sequência de números separados por espaço, aceitando tanto o ponto (.) quanto a vírgula (,) como separadores decimais. O programa deve calcular e exibir a média desses números.

def calcular_media(numeros_usuario):
    """ Esta função calcula a média dos números fornecidos pelo usuário.

    Parâmetros:
        - numeros_usuario: list
            Uma lista de números sobre a qual a média é calculada.

    Retorna: 
        - media: float
            Média dos números na lista
    """
    media = sum(numeros_usuario) / len(numeros_usuario)
    return media

numeros_usuario = ""
while numeros_usuario == "":
    numeros_usuario = input("Digite números separados por espaço: ")
numeros_usuario = numeros_usuario.replace(',', '.').split()
numeros_usuario = [float(num) for num in numeros_usuario]
media = calcular_media(numeros_usuario)
print("Média dos números fornecidos:", media)