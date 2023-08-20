lista = ["banana", "maca", "uva", "cheetos"]

# imprime valores, chaves (indices) são inteiros
for comida in lista:
    print(comida)

print()
    
dicionario1 = {
    "nome": "Rodrigo",
    "idade": 32,
    "altura": 1.7,
}

# imprime chaves
for chave in dicionario1:
    print(chave)

print()

# imprime valores
for chave in dicionario1:
    print(dicionario1[chave])

print()

dicionario2 = {
    "nome": "Marcos",
    "idade": 45,
    "altura": 1.65,
    "endereco": [
        {"local": "trabalho", "numero": 123},
        {"local": "casa", "numero": 57},
    ]
}

for chave in dicionario2:
    print(chave)

print()

for chave in dicionario2:
    print(dicionario2[chave])