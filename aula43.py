intervalo1 = range(3,10,1) # inicio, fim, passo (iterador)
intervalo2 = range(10) # um argumento significa que inicio = 0, passo = 1 e fim = valor do argumento
intervalo3 = range(0,-10,-1) # para intervalos com números negativos, passo também precisa ser negativo

print(intervalo1)
print(intervalo2)

for valor in intervalo3:
    if valor == -5:
        continue
    print(valor, end=" ")
print()
