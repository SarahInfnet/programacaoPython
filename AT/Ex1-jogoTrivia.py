# Objetivo: Criar um jogo de perguntas e respostas (trivia), no qual os jogadores respondem questões de múltipla escolha. 
# Características: O jogo deve ter um banco de, no mínimo, 15 perguntas com 4 alternativas para cada pergunta.
# A cada inicialização do jogo 5 perguntas diferentes devem ser exibidas ao jogador, uma de cada vez,
#e ele deve selecionar uma alternativa.
# O jogo deve indicar se ele acertou ou errou e, após as cinco rodadas, exibir a pontuação do jogador. Se ele acertar
#todas, uma mensagem de parabéns deve ser exibida e uma nova rodada com 5 perguntas diferentes das anteriores deve ser 
#iniciada, até que o jogador erre alguma resposta ou zere o jogo.

import random
import time

# Garantindo que o embaralhamento será diferente a cada execução do script
random.seed(time.time())

perguntas = [
    {
        "pergunta": "Em qual região fica localizado o Rio de Janeiro?",
        "opcoes": ["Nordeste", "Sudeste",  "Amazônia", "Floresta da Tijuca"],
        "resposta": "Sudeste"
    },
    {
        "pergunta": "Qual o nome do melhor amigo do Bob-Esponja?",
        "opcoes": ["Dona Florinda", "Patrick Estrela", "Lula Molusco", "Patrick Estrelado"],
        "resposta": "Patrick Estrela"
    },
    {
        "pergunta": "Quanto tempo a luz do Sol demora para chegar à Terra?",
        "opcoes": ["12 horas", "12 segundos", "8 minutos", "8 horas"],
        "resposta": "8 minutos"
    },
    {
        "pergunta" : "Qual a montanha mais alta do mundo? ",
        "opcoes" : ["Mauna Kea", "Monte Chimborazo", "Pico da Neblina", "Monte Everest"],
        "resposta": "Monte Everest"
    },
    {
        "pergunta" : "Que país tem o formato de uma bota? ",
        "opcoes" : ["Itália ", "Portugal", "México ", "Butão"],
        "resposta" : "Itália "
    },
    {
        "pergunta" : "Quem inventou a lâmpada? ",
        "opcoes" : ["Thomas Edison", "Henry Ford", "Steve Jobs", "Graham Bell"],
        "resposta" : "Thomas Edison"
    },
    {
        "pergunta" : "Quais as duas línguas mais faladas no mundo? ",
        "opcoes" : ["Inglês e espanhol", "Francês e Russo", "Inglês e português", "Inglês e mandarim chinês"],
        "resposta" : "Inglês e mandarim chinês"
    },
    {
        "pergunta" : "Kryptonita é a fraqueza de qual super-herói? ",
        "opcoes" : ["Batman", "Homem-Aranha", "Super-Man", "Shazan"],
        "resposta" :  "Super-Man"
    },
    {
        "pergunta" : "O que os pandas comem? ",
        "opcoes" : ["Carne", "Bambu", "Pizza", "Ração"],
        "resposta" : "Bambu"
    },
    {
        "pergunta" : " Quantos andares tem o maior prédio do mundo? ",
        "opcoes" : ["100", "570", "78", "163"],
        "resposta" : "163"
    },
    {
        "pergunta" : "Em que país foi construído o Muro de Berlim? ",
        "opcoes" : ["Estados Unidos", "Alemanha", "China", "Coreia do Norte"],
        "resposta" :  "Alemanha"
    },
    {
        "pergunta" : "Qual destas substâncias faz parte da composição do vidro? ",
        "opcoes" : ["Areia" , "Álcool" , "Petróleo" , "Fibra"],
        "resposta" :  "Areia"
    },
    {
        "pergunta" : "Quais as respectivas cores da reciclagem do papel, do vidro, do metal e do plástico? ",
        "opcoes" : ["verde, amarelo, azul e vermelho" , "azul, verde, vermelho e amarelo" , "azul, verde, amarelo e vermelho" , "verde, azul, vermelho e amarelo"],
        "resposta" :  "azul, verde, amarelo e vermelho"
    },
    {
        "pergunta" : "Quantos são os personagens principais do seriado norte-americano Friends?",
        "opcoes" : ["2" , "5" , "8" , "6"],
        "resposta" :  "6"
    },
    {
        "pergunta" : "Qual é a comida favorita das tartarugas ninjas? ",
        "opcoes" : ["Pizza" , "Hambúrguer" , "Salada" , "Pepino"],
        "resposta" :  "Pizza"
    }
]

print("-----SEJA BEM-VINDO AO TRIVIA-----")

# Embaralha as perguntas
random.shuffle(perguntas)

perguntas_pendentes = perguntas
errou_alguma_pergunta = False
num_acertos = 0
num_perguntas_feitas = 0

while perguntas_pendentes:
    proximas_perguntas = perguntas_pendentes[:5]
    for dados_pergunta in proximas_perguntas:
        pergunta = dados_pergunta["pergunta"]
        opcoes = dados_pergunta["opcoes"]
        resposta_esperada = dados_pergunta["resposta"]
        while True:
            print(pergunta)
            for i, opcao in enumerate(opcoes, start = 1):
                print(f"{i} - {opcao}")
            try:
                num_resposta_usuario = int(input("Digite o número que corresponde à resposta: "))
                resposta_usuario = opcoes[num_resposta_usuario - 1]
                break
            except (IndexError, ValueError):
                print("Opção inválida!")
        if resposta_usuario == resposta_esperada:
            print("Resposta correta!")
            num_acertos += 1
        else:
            print("Resposta incorreta!")
            errou_alguma_pergunta = True
        num_perguntas_feitas += 1
    
    if errou_alguma_pergunta:
        break

    else:
        print(f"Parabéns! Você concluiu este nível! ")
    perguntas_pendentes = perguntas_pendentes[5:]

print(f"Você acertou {num_acertos} de {num_perguntas_feitas} perguntas!")