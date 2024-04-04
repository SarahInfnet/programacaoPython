#Problema: Implemente uma função que converta a temperatura de Celsius para Fahrenheit.
def converter_celcius_fahrenheit(celcius):
    """
    Esta função transforma a temperatura passada pelo usuário de grau Celsius para Fahrenheit.

    Parâmetros:
        - celcius: float
            Temperatura em graus Celsius
        
    Retorno:
        - fahrenheit: float
            Temperatura em graus Fahrenheit
    """
    fahrenheit = celcius * (9/5) + 32
    return fahrenheit
    

celcius = float(input("Digite um temperatura em graus celcius: "))
fahrenheit = converter_celcius_fahrenheit(celcius)
print(f"A temperatura em grau Celcius é {celcius}°C e convertida para Fahrenheit é {fahrenheit}°F")