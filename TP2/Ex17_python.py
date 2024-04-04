#Problema: Desenvolva um programa que simule a operação de um caixa eletrônico, permitindo ao usuário sacar uma quantia especificada e retornando as notas necessárias para o montante.
def sacar(valor, notas_disponiveis):
    """Esta função simula uma operação em um caixa eletrônico. Em caso de erro, retorna None
    
    Parâmetros:
        - valor: int
            valor que deseja sacar.

        - notas_disponiveis: list
            lista de notas disponíveis.

    Retorno:
        total_cedulas: dict
            quantas cédulas serão necessárias para sacar um valor especifico.
    """
    if valor < 0:
        print("Saldo insuficiente! ")
    total_cedulas = {}
    valor_temp = valor
    for nota in notas_disponiveis:
        quantidade_notas = valor_temp // nota
        valor_temp -= quantidade_notas * nota 
        total_cedulas[nota] = quantidade_notas
    if valor_temp > 0:
        print(f"Não é possível sacar {valor} com as notas {notas_disponiveis}.")
        return None
    return total_cedulas

valor = int(input("Qual valor deseja sacar? (Não é permitido centavos) "))
notas_disponiveis = [200,100,50,20,10,5,2]
cedulas = sacar(valor, notas_disponiveis)
if valor > 0:
    if cedulas is not None:
        print(cedulas)
