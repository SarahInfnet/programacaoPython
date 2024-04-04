#Problema: Escreva uma função que calcule o fatorial de um número passado como argumento e retorne o resultado.
def calcular_fatoreal(num):
    """ Esta função calcula o fatorial de num.

    Parâmetros:
        - num: int
            número que será usado para o cálculo do fatorial.

    Retorna: 
        - resultado: int
            resultado do cálculo fatorial.
    """
    resultado = 1
    for i in range(1,num + 1):
        resultado *= i
    return resultado

num = int(input("Insira um número: "))
print("O fatorial de", num, "é", calcular_fatoreal(num))

