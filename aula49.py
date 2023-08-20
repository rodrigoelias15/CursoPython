lista = ["rodrigo", "maria", "joao"]

indices = range(len(lista))
print(indices)

cont  = 0
for nome in lista:
    print(f"{cont}", nome)
    cont += 1
print()

for indice in indices:
    print(indice, lista[indice])