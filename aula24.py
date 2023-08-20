# Operadores "in" e "not in"

nome = "Rodrigo Oliveira"

# Se possuir caracteres na string, retorna True, do contrário, retorna False
print("Ro" in nome)
print(" " in nome)
print(nome[3])

valor_procurado = input("Digite valor à ser encontrado: ")

if valor_procurado in nome:
    print(f"String \"{nome}\" possui o trecho \"{valor_procurado}\"")
else:
    print(f"Expressão \"{nome}\" não possui \"{valor_procurado}\"")