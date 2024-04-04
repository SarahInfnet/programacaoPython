# Codificador/Decodificador de Mensagens
#Implemente um script que use uma cifra de substituição simples (como a cifra de César) para codificar e decodificar mensagens.

alfabeto_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def obtem_alfabeto_cifrado(deslocamento = 3):
    """
    Gera um alfabeto cujas letras estão deslocadas em relação ao alfabeto convencional.

    Parâmetros:
        - deslocamento: int (default: 3)
    
    Retorna:
        - alfabeto_cifra: str
            Alfabeto com deslocamento.
    """
    alfabeto_cifra = alfabeto_original[deslocamento:] + alfabeto_original[:deslocamento]
    return alfabeto_cifra

def decodifica(frase_codificada, deslocamento = 3):
    """
    Recupera a frase original a partir de uma frase codificada por um dado alfabeto cifrado.

    Parâmetros:
        - frase_codificada: str
            Frase gerada com o alfabeto cifrado
        - deslocamento: int (default: 3)
    
    Retorna:
        - frase_decodificada: str
    """
    alfabeto_cifra = obtem_alfabeto_cifrado(deslocamento)
    cifra_para_letra = {alfabeto_cifra[i]: alfabeto_original[i] for i in range(len(alfabeto_original))} 
    cifra_para_letra[" "] = " "
    frase_codificada = frase_codificada.upper()
    frase_decodificada = ""
    for letra in frase_codificada:
        if letra in cifra_para_letra:
            frase_decodificada += cifra_para_letra[letra]
    return frase_decodificada

def codifica(frase, deslocamento = 3):
    """
    Codifica a frase utilizando um alfabeto cifrado.

    Parâmetros:
        - frase: str
            Frase gera ser codificada.
        - deslocamento: int (default: 3)
    
    Retorna:
        - frase_codificada: str
    """
    alfabeto_cifra = obtem_alfabeto_cifrado(deslocamento)
    letra_para_cifra = {alfabeto_original[i]: alfabeto_cifra[i] for i in range(len(alfabeto_original))}
    letra_para_cifra[" "] = " "

    frase = frase.upper()
    frase_codificada = "" 
    for letra in frase:
        if letra in letra_para_cifra:
            frase_codificada += str(letra_para_cifra[letra]) 
    return frase_codificada.strip()

selecao = int(input("Deseja codificar ou decodificar uma frase: (1- codificar/ 2- decodificar) "))
if selecao == 1:
    frase_original = input("Digite uma frase (sem acento ou Ç): ")
    frase_codificada = codifica(frase_original)
    print(frase_codificada)
elif selecao == 2:
    frase_cifra_substituicao = input("Digite uma frase cifrada: ")
    frase_decodificada = decodifica(frase_cifra_substituicao)
    print(frase_decodificada)
else:
    print("Digite uma opção válida! ")