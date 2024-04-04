#Problema: Desenvolva um programa que converta um número da base decimal para binária usando um loop while.
decimal_usuario = int(input("Digite um número decimal: "))
def converte_decimal_binario(decimal):
    """ Esta função converte um decimal para um número binário.

    Parâmetros:
        - decimal: int
            número decimal utilizado para a transformação em binário.

    Retorna: 
        - binario: str
            decimal já transformado em binário.
    """
    binario = ""
    if decimal_usuario == 0:
        return 0
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
            
    return binario

binario_resultado = converte_decimal_binario(decimal_usuario)
print(f'O número binário é: {binario_resultado}')
