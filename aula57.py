# Buscando item dentro de uma lista dentro de outra lista
# Entre parênteses é uma tupla

lista = ["rodrigo", ["nome", "casaco"], 51, ["eduardo", "monica", (0, 10, 20, 30, 40)]]

print(lista[1][0])

print(lista[3][2][4])
