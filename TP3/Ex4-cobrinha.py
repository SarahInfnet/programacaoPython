# Decodificador de Código Morse
# Implemente um programa que traduza uma string de código Morse para texto e vice-versa.

letraParaMorse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--","N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "/": "-..-.", " ": "/"
}

morseParaLetra = {v: k for k, v in letraParaMorse.items()}

def decodifica(frase_codificada):
    """Decodifica uma frase em código Morse.

    Parâmetros:
        - frase_codificada: str
            A frase em código Morse, onde cada caractere é separado por um espaço em branco.

    Retorna:
        - frase_decodificada: str
            A frase decodificada.
    """
    frase_decodificada = "" 
    frase_codificada = frase_codificada.split(" ")
    for letra in frase_codificada:
        if letra in morseParaLetra:
            frase_decodificada += morseParaLetra[letra]
    return frase_decodificada

def codifica(frase):
    """Converte uma frase para código Morse.

    Parâmetros:
        - frase: str
            A frase a ser codificada.

    Retorna:
        - frase_codificada: str
            A frase em código Morse, onde cada caractere é separado por um espaço em branco.
    """
    frase = frase.upper()
    frase_codificada = "" 
    for letra in frase:
        if letra in letraParaMorse:
            frase_codificada += letraParaMorse[letra] + " "
    return frase_codificada

escolha = int(input("Deseja codificar ou decodificar uma frase: (1- codificar/ 2- decodificar) "))
if escolha == 1:
    frase_original = input("Digite uma frase (sem acento ou Ç): ")
    frase_codificada = codifica(frase_original)
    print(frase_codificada)
elif escolha == 2:
    frase_codigo_morse = input("Digite uma frase em cógigo morse: ")
    frase_decodificada = decodifica(frase_codigo_morse)
    print(frase_decodificada)
else:
    print("Digite uma opção válida! ")
