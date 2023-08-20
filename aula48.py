lista1 = ["rodrigo", 1, 1.5, []]
num = 5
lista_vazia = []

print("Lista vazia:",lista_vazia)
print("Lista:", lista1)
print("Elemento \"2\" da lista:", lista1[2])
print("Variavel num =", num)

del num # "del" deleta objetos, pode ser o item de uma lista, uma lista inteira, uma variável, etc
print("item \"2\" removido da lista")
del lista1[2]

print("Item \"str\" adicionado ao fim da lista")
lista1.append("str") # adiciona item no final da lista
print(lista1)

print("Ultimo item removido da lista")
lista1.pop() # remove ultimo item da lista
print("Item \"0\" removido da lista")
lista1.pop(0) # remove item especificado no argumento
print(lista1)
print("Item \"1\" alterado")
lista1[1] = "teste" # altera elemento
print(lista1)
print("Adicionado elemento na posição \"0\"")
lista1.insert(0, "ola mundo")
print(lista1)

lista2 = [1, 2, 3]
lista2.extend(lista1) # extende lista com lista que está no argumento
print(lista2)

try:
    print(num)
except:
    print("ERRO! Tentou imprimir \"num\" mas foi deletado")