#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.
contador = {
    "hamburguer":{
        "nome": "Hamburguer",
        "votos": 0
    },

    "cachorro-quente":{
        "nome": "Cachorro-quente",
        "votos": 0
    },

    "pizza":{
        "nome": "Pizza",
        "votos": 0
    },

}
quantidade_votos = int(input("Quantos votos serão registrados? "))
for i in range(quantidade_votos):
    voto_usuario = input("Qual desses é a melhor opção? (hamburguer, cachorro-quente ou pizza) ")
    contador[voto_usuario]["votos"] += 1 
print(contador["hamburguer"]["nome"], contador["hamburguer"]["votos"])
print(contador["cachorro-quente"]["nome"], contador["cachorro-quente"]["votos"])
print(contador["pizza"]["nome"], contador["pizza"]["votos"])