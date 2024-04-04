# Objetivo: Criar um aplicativo que permita ao usuário monitorar suas despesas e receitas, categorizar gastos e 
#visualizar um resumo financeiro.

# Características: O sistema deverá permitir ao usuário:

# Inicialmente, definir seu saldo atual;
# Adicionar valores (receitas) ao seu orçamento, descrevendo a fonte financeira com um texto;
# Anotar gastos (despesas) que deverão ser associados a categorias pré-definidas como alimentação, transporte, 
# lazer, etc e, opcionalmente, após o valor, separado por “;” o usuário poderá escrever um texto associado a este gasto.
# Solicitar um relatório dos gastos, tipo extrato, que liste todas entradas e saídas indicando o saldo da conta 
# a cada operação e o saldo final;
# Solicitar um relatório ordenado por valor dos gastos por categoria;
# Solicitar um relatório com todas as receitas.

movimentos = []
lista_categorias = ["Alimentação", "Transporte", "Lazer", "Educação", "Contas", "Outros"]

def registra_movimento(movimentos, tipo, valor, desc = None, categoria = None):
    """ Adiciona um movimento(entrada ou saida) de uma conta
    
    Parâmetros:
        movimentos: list
            - Uma lista onde cada elemento corresponde a um dicionário

        tipo: str
            - entrada ou saida 
        
        valor: float
            - valor da despesa ou da receita

        desc: str (default: None)
            - descrição da ação efetuada

        categoria: str (default: None)
            - categoria que deseja associar

    """
    movimento = {"tipo": tipo, "valor": valor, "desc": desc, "categoria": categoria}
    movimentos.append(movimento)

def exibe_extrato(saldo_atual):
    """ Exibe todas as entradas e saídas indicando o saldo da conta a cada operação
    
    Parâmetros:
        saldo_atual: float
            - saldo atualizado

    """
    print()
    print("----------------------- Extrato -----------------------")
    for movimento in movimentos:
        if movimento["tipo"] == "entrada":
            saldo_atual = saldo_atual + movimento["valor"]            
            print(f"{movimento["desc"]}: + R$ {movimento["valor"]:.2f}")
            print(f"Saldo atual: R$ {saldo_atual:.2f}")
            print()
        else:
            saldo_atual = saldo_atual - movimento["valor"]
            print(f"Categoria: {movimento["categoria"]} \nValor: - R$ {movimento["valor"]:.2f} \nDescrição: {movimento["desc"]}")
            print(f"Saldo atual: R$ {saldo_atual:.2f}")
            print()
    print("-------------------------------------------------------")
    

def exibe_receita():
    """ Exibe todas as entradas """
    print()
    print("----------------------- Receitas -----------------------")
    for movimento in movimentos:
        if movimento["tipo"] == "entrada":
            print(f"{movimento["desc"]}: R$ {movimento["valor"]:.2f}")

def exibe_gastos_categoria():
    """ Exibe um relatório ordenado por valor dos gastos por categoria"""
    print()
    print("----------------------- Gastos -----------------------")
    # Acumula gastos por categoria
    gastos_categorias = {}
    for movimento in movimentos:
        if movimento["tipo"] == "saida":
            categoria = movimento["categoria"] 
            valor = movimento["valor"]
            if categoria in gastos_categorias:
                gastos_categorias[categoria] += valor
            else:
                gastos_categorias[categoria] = valor
                
    #ordena de acordo com o valor gasto em cada categoria
    gastos_ordenados = sorted(gastos_categorias.items(), key = lambda categoria_valor: -categoria_valor[1])

    # Exibe gastos acumulados por categoria
    for categoria, valor in gastos_ordenados:
        print(f"{categoria}: R$ {valor:.2f}")
    

def menu():
    """ Exibe o menu para o usuário"""
    while True:
        try:
            print()
            escolha_usuario = int(input("1 - Adicionar despesas \n2 - Adicionar receitas \n3 - Exibir extrato \n4 - Exibir receitas \n5 - Exibir gastos por categoria \n6 - Sair \nEscolha uma opção: "))
            if escolha_usuario == 1:
                print()
                print("1 - Alimentação \n2 - Transporte \n3 - Lazer \n4 - Educação \n5 - Contas \n6 - Outros")
                escolha_categoria_usuario = int(input("Escolha uma categoria: "))
                categoria = lista_categorias[escolha_categoria_usuario - 1]
                despesa_fonte = input("Digite o valor da despesa e opcionalmente um texto separado por ';' ").strip()
                if ";" in despesa_fonte:
                    despesa_fonte = despesa_fonte.split(";")
                    valor = int(despesa_fonte[0])
                    desc = despesa_fonte[1]
                else: 
                    valor = int(despesa_fonte)
                    desc = None
                    
                registra_movimento(movimentos, "saida", valor, desc, categoria)
                        

            elif escolha_usuario == 2:
                valor = float(input("Digite o valor a ser adicionado: "))
                desc = input("Digite a fonte financeira: ")
                registra_movimento(movimentos, "entrada", valor, desc)
        
            elif escolha_usuario == 3:
                exibe_extrato(saldo_atual)

            elif escolha_usuario == 4:
                exibe_receita()

            elif escolha_usuario == 5:
                exibe_gastos_categoria()

            elif escolha_usuario == 6:
                break

            else:
                print("Escolha uma opção válida! ")
        except:
            print("Verifique se digitou corretamente conforme orientado.")

while True:
    try:
        saldo_atual = float(input("Digite seu saldo atual: "))
        break
    except:
        print("Verifique se digitou somente números.")
        
menu()
