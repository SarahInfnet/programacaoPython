# Validador de Senhas
# Crie um script que valide e classifique a complexidade de uma senha baseado em critérios definidos (ex: mínimo de caracteres maiúsculos e minúsculos, uso de números e símbolos).

alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = alfabeto_minusculo.upper()
lista_numeros = "0123456789"
lista_caractere_especial = "@!#$$&*-+=?"

def valida_senha(senha, caractere_especial = True, numero = True, maiusculo = True, minusculo = True, tamanho_minimo = 8):
    """Valida a senha de acordo com critérios definidos.

    Parâmetros:
        - senha: str
        - caractere_especial: bool (default: True)
        - numero: bool (default: True)
        - maiusculo: bool (default: True)
        - minusculo: bool (default: True)
        - tamanho_minimo: int (default: 8)

    Retorna: 
        - resultado_validacao: bool
            True se satisfaz todas as condições. False, caso contrário.
    """
    if caractere_especial == True:
        tem_caractere_especial = False
        for caractere in senha:
            if caractere in lista_caractere_especial:
                tem_caractere_especial = True
                break
        if not tem_caractere_especial:
            return False

    if numero == True:
        tem_numero = False
        for caractere in senha:
            if caractere in lista_numeros:
                tem_numero = True
                break
        if not tem_numero:
            return False

    if maiusculo == True:
        tem_maiusculo = False
        for caractere in senha:
            if caractere in alfabeto_maiusculo:
                tem_maiusculo = True
                break
        if not tem_maiusculo:
            return False
       
    if minusculo == True:
        tem_minusculo = False
        for caractere in senha:
            if caractere in alfabeto_minusculo:
                tem_minusculo = True
                break
        if not tem_minusculo:
            return False

    if len(senha) < 8:
            return False

    return True 

def classifica_senha(senha):
    """Classifica a senha em uma das quatro classes: fraca, média, forte ou muito forte. 

    Parâmetros:
        - senha: str

    Retorna: 
        - classificacao: str
            fraca, média, forte ou muito forte.
    """
    tamanho = len(senha)
    tem_caractere_especial = False
    tem_numero = False
    tem_maiusculo = False
    tem_minusculo = False
    
    for caractere in senha:
        if caractere in lista_caractere_especial:
            tem_caractere_especial = True
        if caractere in lista_numeros:
            tem_numero = True
        if caractere in alfabeto_maiusculo:
            tem_maiusculo = True
        if caractere in alfabeto_minusculo:
            tem_minusculo = True

    pontos = tem_caractere_especial + tem_numero + tem_maiusculo + tem_minusculo

    if tamanho < 5:
        if pontos == 4:
            return "media"
        else:
            return "fraca"
        
    elif tamanho < 8:
        if pontos >= 3:
            return "forte"
        else:
            return "media"

    else:
        if pontos == 4:
            return "muito forte"
        else: 
            return "forte"

senha = input("Digite a senha: ")
validacao_resultado = valida_senha(senha)
if validacao_resultado == True:
    print("Senha válida!")
else: 
    print("Senha inválida!")
    
classificao_resultado = classifica_senha(senha)
print("Sua senha é:", classificao_resultado)