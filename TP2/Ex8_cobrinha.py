#Problema: Escreva uma função que calcule a potência de um número com um expoente padrão de 2, permitindo ao usuário alterar esse expoente com parâmetros por Keyword e retorne o resultado da operação. 

numero = float(input("Insira um número: "))
expoente = float(input("Insira um expoente: "))

def calcularPotencia(numero, expoente = 2):
    """
    Retorna numero**expoente.

    Parâmetros: 
        - numero: float
            A base da potenciação.

        - expoente: float (default: 2)
            O expoente da potenciação.

    Retorna: 
        - resultado: float
            O resultado da potenciação, ou seja, numero**expoente
    """
    resultado = numero ** expoente
    return resultado

print("Com valor padrão de expoente 2:") 
print(calcularPotencia(numero))
print(f"Com valor do expoente {expoente}: ") 
print(calcularPotencia(numero,expoente))


