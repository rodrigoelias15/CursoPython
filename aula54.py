
lista = []

while True:
    
    opcao = input("Selecione uma opção, [i]nsira, [d]elete ou [a]ltere um item da lista, [e]xiba a lista ou digite [s]air: ").lower()
    
    if opcao == "i":
        item = input("Digite um item para colocar na lista: ")
        lista.append(item)
    elif opcao == "d":
        i = input("Digite indice do item que é para deletar: ")
        i = int(i)
        lista.pop(i)
    elif opcao == "a":
        i = input("Digite indice do item que é para alterar: ")
        item = input("Digite nome do novo item: ")
        lista[i] = item
    elif opcao == "s":
        break
    elif opcao == "e":
        print(lista)
    else:
        print("Digite opção correta.")
        continue