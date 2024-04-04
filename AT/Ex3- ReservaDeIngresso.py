#Objetivo: Criar um sistema que simule a interface de um serviço de reservas de ingressos para um cinema, e que permita
#ao usuário escolher entre os filmes em cartaz no cinema, selecionar entre os assentos disponíveis e fazer 
#a reserva de ingressos. 

# Características: O sistema deve fornecer uma visualização gráfica dos assentos disponíveis que pode ser implementada 
# com uma interface gráfica ou por diagramas em texto que dê ao usuário uma visão da posição dos assentos em relação à
# tela, assentos já ocupados, assentos livres e assentos selecionados. Os lugares devem ser marcados por fileiras em ordem
# alfabética e a posição de cada cadeira por um número. O programa deverá solicitar o nome do próximo cliente 
#para que este faça sua reserva ou um comando de saída que deverá retornar uma estrutura de dados que outra aplicação
#usaria para manipular o banco de dados de assentos, associando estes assentos ao nome do comprador.

filmes_cartaz = ["Barbie", "Kung Fu Panda 4", "Duna 2", "The Chosen"]
assentos_reservas = {
    filme: {
        linha: {
            coluna: None for coluna in range(1, 10)
        } for linha in ["A", "B", "C", "D", "E", "F"]
    } for filme in filmes_cartaz
}

def exibe_assentos(assentos_sala):
    """ Exibe todos os assentos
    
    Parâmetros:
        assentos_sala: dict
            representa os assentos de uma sala de cinema.
    """
    print(" ", end=" ")
    for coluna in assentos_sala["A"]:
        print(coluna, end=" ")
    print()
    for linha in assentos_sala:
        cadeiras_linha = assentos_sala[linha]
        print(linha, end=" ")
        for coluna in cadeiras_linha:
            status = assentos_sala[linha][coluna]
            if status is not None:
                print("#", end =" ")
            else:
                print("*", end=" ")
        print()
    print("Legenda: * - Livre | # - Ocupado")

def reserva(assentos_sala, linha, coluna, nome):
    """Verifica se o assento está disponível e faz a reserva

    Paramêtros: 
        assentos_sala: dict
            representa os assentos de uma sala de cinema.

        linha: str
            representa a fileira do assento a ser reservado.

        coluna: int
            representa a coluna do assento a ser reservado.

        nome: str
            nome da pessoa que esta reservando o assento.
    """
    try:
        status = assentos_sala[linha][coluna]
        if status is not None:
            print("O assento escolhido está ocupado. Escolha outro assento!")
            return False
        else:
            assentos_sala[linha][coluna] = nome
            print("Assento reservado com sucesso! Aproveite o filme!")
            return True
    except KeyError:
        print("Você escolheu um assento inválido.")


def verifica_reserva(nome):
    """Retorna todas as reservas associadas ao nome passado passado como parâmetro. Caso não haja nenhuma reserva, retorna None.

    Paramêtros: 
        nome: str
            - nome da pessoa cujas reservas estao sendo consultadas.

    Retorno: 
        reservas: str ou None
            as reservas associadas ao nome consultado.
    """
    reservas = ""
    for filme in assentos_reservas:
        for linha in assentos_reservas[filme]:
            for coluna in assentos_reservas[filme][linha]:
                reservadoPor = assentos_reservas[filme][linha][coluna]
                if reservadoPor is not None:
                    if reservadoPor.lower() == nome.lower():
                        reservas += f"- Filme '{filme}', assento {linha}{coluna}\n"
    if reservas == "":
        return None
    return reservas

def menu():
    """ Exibe o menu para o usuário"""
    while True:
        try:
            print("O que deseja fazer?")
            escolha_usuario = int(input("1 - Fazer reserva | 2 - Verificar reserva | 3 - Sair "))
        except: 
            print("Verifique se digitou corretamente.")

        if escolha_usuario == 1:
            while True:
                try:
                    print("Qual filme deseja assistir? ")
                    for i, filme in enumerate(filmes_cartaz, start = 1):
                        print(f"{i} - {filme}")
                    num_resposta_usuario = int(input("Digite o número que corresponde à resposta: "))
                    filme = filmes_cartaz[num_resposta_usuario - 1]
                    break
                except:
                    print("Verifique se digitou uma opcão corretamente.")
                    print()

            assentos_sala = assentos_reservas[filme]
            nome = input("Digite seu nome: ")
            exibe_assentos(assentos_sala)
            try:
                linha, coluna = input("Qual assento deseja escolher? (Ex: B 10, E 5) ").strip().upper().split(" ")
                coluna = int(coluna)
                resultado_reserva = reserva(assentos_sala, linha, coluna, nome)
                if resultado_reserva == True:
                    print(f"Reserva realizada para o filme {filme} e o assento {linha}{coluna}")
                else:
                    print(f"Não foi possível realizar a reserva. Verifique se você selecionou um assento disponível.")
            except:
                print("Verifique se você digitou a linha e a coluna do assento corretamente, separados por um espaço.")

        elif escolha_usuario == 2:
            nome = input("Digite seu nome: ")
            reservas = verifica_reserva(nome)
            if reservas:
                print(reservas)
            else:
                print("Não foram encontradas reservas para o nome informado.")

        elif escolha_usuario == 3:
            print("Saindo, tenha um bom dia!")
            break

        else:
            print("Escolha uma opção válida!")

print("Seja bem-vindo!")
menu()
