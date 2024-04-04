#Problema: Crie um programa que concatene duas listas fornecidas pelo usuário e organize a lista em ordem crescente. 

lista1 = []
lista2 = []
quantidade_itens_lista1 = int(input("Quantos itens deseja inserir na lista 1? "))
quantidade_itens_lista2 = int(input("Quantos itens deseja inserir na lista 2? "))
for i in range(quantidade_itens_lista1):
    adicionar_item_lista1 = input("Digite qual item deseja inserir na lista 1: ").lower()
    lista1.append(adicionar_item_lista1)

for i in range(quantidade_itens_lista2):
    adicionar_item_lista2 = input("Digite qual item deseja inserir na lista 2: ").lower()
    lista2.append(adicionar_item_lista2)
    
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
lista_concatenada = lista1 + lista2
print(f"Lista concatenada: {lista_concatenada}")
lista_concatenada.sort()
print(f"Lista ordenada: {lista_concatenada}")