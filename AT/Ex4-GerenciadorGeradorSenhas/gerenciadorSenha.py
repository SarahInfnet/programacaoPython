# Objetivo: Criar um programa que gere senhas fortes aleatoriamente, com comprimento definido pelo usuário e as armazene 
# em uma estrutura de dados criptografada.

# Características: O banco de dados deve armazenar o nome do serviço, o username de login e a senha, sendo todas as
# informações armazenadas utilizando um método simples de criptografia (pode ser algo similar à cifra de César). 
# O usuário deverá entrar com o nome do serviço, o username e o comprimento da senha para gerar a senha. E deve ser 
# implementada uma função de consulta que solicite ao usuário o nome do serviço e exiba a ele o username e senha salva
# após responder corretamente à uma palavra chave (que pode estar exposta no código para este exemplo).

from cifraCesar import decodifica, codifica
from geradorSenha import gerador_senha

def consulta(nome_servico, deslocamento_cifra, dados_usuario):
    """ Verifica se existe algum registro para o serviço consultado.

    Paramêtros:
        - nome_servico = str
            nome do serviço 

        - deslocamento_cifra: int
            quantas posições os caracteres serão deslocados pra direita. É usado para decriptografar os dados armazenados em dados_usuario.

        - dados_usuario: list
            lista de dicionarios onde estão salvos os dados de todos os usuários e serviços.

    Retorna: 
        - registros_encontrados: list
            lista dos registros encontrados para o serviço consultado.
    """
    registros_encontrados = []
    for dados in dados_usuario:
        nome_servico_registro = decodifica(dados["nome_servico"], deslocamento_cifra)
        if nome_servico.lower() == nome_servico_registro.lower():
            registros_encontrados.append({k: decodifica(v, deslocamento_cifra) for k, v in dados.items()})
    return registros_encontrados

def registra(nome_servico, username, senha, deslocamento_cifra, dados_usuario):
    """ Registra uma conta na lista dados_usuario

    Paramêtros:
        - nome_servico = str
            nome do serviço 

        - username: str
            nome de usuário
            
        - senha: list
            senha do usuario

        - deslocamento_cifra: int
            quantas posições os caracteres serão deslocados pra direita. É usado para criptografar os dados antes que ele seja armazenado em dados_usuario

        - dados_usuario: list
            lista de dicionarios onde serão salvos os dados do usuario.
    """
    nome_servico_cifrado = codifica(nome_servico, deslocamento_cifra)
    username_cifrado = codifica(username, deslocamento_cifra)
    senha_gerada_cifrada = codifica(senha, deslocamento_cifra)
    dados_usuario.append(
        {
            "nome_servico": nome_servico_cifrado, 
            "username": username_cifrado, 
            "senha": senha_gerada_cifrada
        }
    )
    print("Registrado com sucesso!")

def exibe_registro_usuario(registro):
    """Exibe um registro na tela do usuário.
    
    Paramêtros:
        - registro: dict
            Contém os dados de um registro, isto é, o nome do serviço, o nome de usuário e a senha.
    
    """
    print(f'Nome de serviço: {registro["nome_servico"]}')
    print(f'Username: {registro["username"]}')
    print(f'Senha: {registro["senha"]}')

def menu(dados_usuario, deslocamento_cifra, palavra_chave):
    """Exibe o menu para o usuario.
    
    Paramêtros:

        - dados_usuario: list
            lista de dicionarios onde serão salvos os dados do usuario.

        - deslocamento_cifra: int
            quantas posições os caracteres serão deslocados pra direita.
    
        - palavra_chave: str
            chave para acessar os registros criptografados
    """
    print("Seja Bem-Vindo! O que deseja fazer? ")
    while True:
        try:
            opcao_escolhida = int(input("1 - Registrar conta | 2 - Consultar conta | 3 - Exibir registros criptografados | 4 - Sair "))

            if opcao_escolhida == 1:
                nome_servico = input("Digite o nome de serviço: ")
                username = input("Digite o nome de login: ")
                tamanho = int(input("Qual o tamanho da senha? "))
                senha_gerada = gerador_senha(tamanho)
                registra(nome_servico, username, senha_gerada, deslocamento_cifra, dados_usuario)

            elif opcao_escolhida == 2:
                palavra_chave_usuario = input("Digite a palavra-chave para consultar os dados: ")
                if palavra_chave_usuario == palavra_chave:
                    nome_servico = input("Digite o nome de serviço: ")
                    resultados_consulta = consulta(nome_servico, deslocamento_cifra, dados_usuario)
                    if resultados_consulta:
                        print()
                        print(f"{len(resultados_consulta)} resultado(s) encontrado(s).")
                        print()
                        for registro in resultados_consulta:
                            exibe_registro_usuario(registro)
                            print()
                    else:
                        print("Não há nenhum registro para o serviço informado.")
                else:
                    print("Palavra-chave incorreta!")

            elif opcao_escolhida == 3:
                print(dados_usuario)
                print()

            elif opcao_escolhida == 4:
                print("Saindo! Obrigada,tenha um bom dia!")
                break
            
            else:
                print("Escolha uma opção válida!")

        except:
            print("Verifique se digitou corretamente.")

dados_usuario = []
deslocamento_cifra = 3
palavra_chave = "password"
menu(dados_usuario, deslocamento_cifra, palavra_chave)