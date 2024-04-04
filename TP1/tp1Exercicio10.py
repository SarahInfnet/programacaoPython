#Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random
personagens = ["Homem-aranha", "Bob esponja", "Hulk", "Mickey Mouse", "Branca de neve", "Nemo", "Woody"]
acoes = ["correu","dançou","esmagou", "brincou","cantou","nadou","se aventurou"]
locais = ["na rua", "na fenda do biquini", "em Nova York", "na sua casa", "na floresta", "no mar", "na creche"]
personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)
historia = f"{personagem} {acao} {local}."
print(historia)