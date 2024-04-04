#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

personagens = {
    "homem-aranha": {
        "nome": "Homem-aranha",
        "apresentacao": "Você era uma pessoa qualquer, mas foi mordido por uma aranha e ganhou super poderes.",
        "fraseDeEfeito": "Ser herói não é apenas sobre superpoderes, é sobre fazer a coisa certa!"
    },

    "homem de ferro": {
        "nome": "Homem de ferro",
        "apresentacao": "De um bilionario para super heroi, utilizando seus recursos e inteligencia voce construiu um traje e dedicou para salvar o planeta.",
        "fraseDeEfeito": "A melhor defesa é um bom ataque, e eu sou um excelente atacante!"
    },

    "hulk":{
        "nome": "Hulk",
        "apresentacao": "De um experimento a homem mais forte do planeta. Com sua força esmagadora combate inimigos e os reduz a nada",
        "fraseDeEfeito": "Hulk esmaga!"
    }
}

inimigos = {
    "duende verde":{
        "nome": "Duende verde",
        "apresentacao": "Norman Osborn, um rico e poderoso que, após um experimento que deu errado, adquiriu habilidades sobre-humanas e uma personalidade dividida.",
        "fraseDeEfeito": "A cidade vai tremer diante do Duende Verde!"
    },
    
    "thanos":{
        "nome": "Thanos",
        "apresentacao": " Um titã, tem uma imensa força física, e também inteligência e habilidades estratégicas.",
        "fraseDeEfeito": "Aqueles que se opõem a mim são apenas poeira no vento do destino!"
    },

    "magneto":{
        "nome": "Magneto",
        "apresentacao": " Um mutante poderoso que tem a capacidade de controlar campos magnéticos. ",
        "fraseDeEfeito": "O poder reside naqueles que têm a coragem de reivindicá-lo."
    }
}

while True:
    personagem_escolhido_str = input(f"Escolha um personagem: {list(personagens.keys())} ")

    if personagem_escolhido_str in personagens:
        personagem_escolhido = personagens[personagem_escolhido_str]
        break
    else:
        print("Por favor escolha uma opção existente.")

print(personagem_escolhido["nome"])
print(personagem_escolhido["apresentacao"])    
print("Ao observar a cidade, você vê uma movimentação estranha, pessoas gritando e o caos se instalando. Apressado você chega ao local e vê seu maior inimigo!")

while True:
    inimigo_escolhido_str = input(f"Escolha um inimigo: {list(inimigos.keys())} ")
    if inimigo_escolhido_str in inimigos:
        inimigo_escolhido = inimigos[inimigo_escolhido_str]
        break
    else:
        print("Por favor escolha uma opção existente ou digite corretamente.")

print(inimigo_escolhido["nome"])
print(inimigo_escolhido["apresentacao"])   

print(f"Você corre em direção ao {inimigo_escolhido["nome"]} e iniciam uma briga, com socos e golpes de ambos os lados, a batalha parece estar equilibrada, mas um golpe final pode determinar quem irá ganhar a batalha.")

golpe_final = input("Escolha o golpe final: (Força Interior ou Investida Fatal)")
if golpe_final.lower() == "força interior":
    print(f"{personagem_escolhido["nome"]} invoca sua força interior, coragem e determinação para executar um ataque rápido e preciso, surpreendendo o {inimigo_escolhido["nome"]} com um golpe perfeito. Com o pé ainda em cima do inimigo, {personagem_escolhido["nome"]} diz '{personagem_escolhido["fraseDeEfeito"]}'. {inimigo_escolhido["nome"]} é vencido e {personagem_escolhido["nome"]} salva o dia mais uma vez! ")
if golpe_final.lower() == "investida fatal":
    print(f" {personagem_escolhido["nome"]} em um ato de desespero, lança um ataque final e desesperado contra {inimigo_escolhido["nome"]}. No entanto, essa tentativa desesperada acaba esgotando completamente suas energias e deixando-o vulnerável a um contra-ataque devastador. {inimigo_escolhido["nome"]} ganha a batalha e diz '{inimigo_escolhido["fraseDeEfeito"]}', deixando {personagem_escolhido["nome"]} caido no chão.")

