#Problema: Crie um programa que valide um número de CPF fornecido pelo usuário (considerando apenas a validação dos dígitos verificadores).
cpf = input("Digite seu CPF: (sem pontução) ")

def validar_cpf(cpf):
    """ Esta função valida os dois últimos digitos verificadores de um cpf.

    Parâmetros:
        - cpf: str
            String que representa o cpf passado pelo usuário.
    
    Retorno:D
        - cpfTemp == cpf: bool
            verifique se o cpfTemp já validado é igual ao cpf passado pelo usuário.
    """
    if len(cpf) != 11:
        print("O CPF deve conter 11 dígitos")
        return False
    
    cpfTemp = cpf[:-2]
    
    # 1) Calcule a soma dos produtos dos nove digitos utilizando peso dois para unidade, peso 3 para dezena, peso 4 para centena e assim sucessivamente. 
    pesos = list(range(10,1,-1))

    soma_passo1 = 0
    for i in range(9):
        soma_passo1 += int(cpfTemp[i]) * pesos[i]

    # 2) A dezena do número verificador é 0 caso o resto da divisão por 11 da soma dos produtos seja 0 ou 1; caso contrario a dezena corresponde  a subtrair de 11 o resto da divisão por 11 da soma dos produtos.
    resto = soma_passo1 % 11
    if  resto == 0 or resto == 1:
        primeiro_digito_verificador = 0    
    else:
        primeiro_digito_verificador = 11 - resto

    cpfTemp += str(primeiro_digito_verificador)

    # 3) Calcule a soma dos produtos dos dez digitos, onde o digito menos significativo passa a ser a dezena dos digitos verificadores, utilizando os seguintes pesos: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    pesos = list(range(11,1,-1))

    soma_passo3 = 0
    for i in range(10):
        soma_passo3 += int(cpfTemp[i]) * pesos[i]


    # 4) A unidade do número verificador é 0 caso o resto da divisão da soma dos produtos seja 0 ou 1; caso contrário a unidade corresponde a 11 menos o resto da divisão por 11 da soma dos produtos.
    resto = soma_passo3 % 11
    if  resto == 0 or resto == 1:
        segundo_digito_verificador = 0    
    else:
        segundo_digito_verificador = 11 - resto

    cpfTemp += str(segundo_digito_verificador) 

    return cpfTemp == cpf

digito_verificador = cpf[-2:]
print(validar_cpf(cpf))