# Substituidor de Palavras em Texto
# Escreva um programa que substitua todas as ocorrências de uma palavra específica em um texto por outra palavra fornecida pelo usuário.

def substitui(frase_usuario, palavra_a_ser_substituida, palavra_nova):
    """Substitui todas as ocorrências de uma palavra específica em um texto por outra palavra.

    Parâmetros:
        - frase_usuario: str
        - palavra_a_ser_substituida: str
        - palavra_nova: str    

    Retorna: 
        - nova_frase: str
            Frase com as devidas substituições.
    """
    if palavra_a_ser_substituida in frase_usuario:
        nova_frase = frase_usuario.replace(palavra_a_ser_substituida, palavra_nova)
        return nova_frase
    else:
        return None

frase_usuario = input("Digite uma frase: ").lower()
palavra_a_ser_substituida = input("Qual palavra deseja substituir? ").lower()
palavra_nova = input("Qual a nova palavra? ").lower()
nova_frase = substitui(frase_usuario, palavra_a_ser_substituida, palavra_nova)

if nova_frase is None:
    print("Esta palavra não pode ser substituida, pois não existe!")

else: 
    print(nova_frase)