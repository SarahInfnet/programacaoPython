# Conversor de Números Romanos
# Faça um programa que converta um número romano para um número decimal e vice-versa.

numero_para_romano = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC", 
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM", 4000: "IV\u0305", 5000: "V\u0305", 6000: "VI\u0305", 7000: "VII\u0305", 8000: "VIII\u0305", 9000: "IX\u0305", 
    10000: "X\u0305" 
}

romano_para_numero = {v: k for k, v in numero_para_romano.items()}

def decodifica(numero_romano):
    """Converte um número romano para um número decimal.

    Parâmetros:
        - numero_romano: str
            Uma string representando o número romano.

    Retorna:
        - numero_decodificado: int
            O número convertido para o sistema de algarismos arábico.
    """
    nao_mapeado = numero_romano
    numero_decodificado = 0
    while nao_mapeado != "":
        digito_romano = nao_mapeado
        while not digito_romano in romano_para_numero:
            digito_romano = digito_romano[:-1]
        numero_decodificado += romano_para_numero[digito_romano]
        nao_mapeado = nao_mapeado[len(digito_romano):]
    return numero_decodificado

def codifica(numero_original):
    """Converte um número no sistema de algarismos arábico para o sistema romano.

    Parâmetros:
        - numero_original: int
            O número a ser convetido.

    Retorna:
        - numero_codificado: str
            Uma string representando o número romano.
    """
    numero_codificado = ""
    numero_original = str(numero_original)
    total_digitos = len(numero_original)
    for i in range(total_digitos):
        digito = int(numero_original[i])
        expoente = total_digitos - 1 - i
        digito_peso = digito * 10**expoente
        digito_codificado = numero_para_romano[digito_peso]
        numero_codificado += digito_codificado 
    return numero_codificado

escolha = int(input("1- converter um numero para romano/ 2- converter de romano para numero: "))
if escolha == 1:
    numero_original = int(input("Digite um numero: "))
    numero_codificado = codifica(numero_original)
    print(numero_codificado)

elif escolha == 2:
    numero_romano = input("Digite um número romano: ")
    numero_decodificado = decodifica(numero_romano)
    print(numero_decodificado)
else:
    print("Digite uma opção válida! ")
