# Operadores lógicos and, or e not

if 10 == 10 and 13 > 20 and 15 < 20:
    print("Todas condições são verdadeiras")
else:
    print("Uma das condições falhou")


# 0 ou string vazia, sem espaços ('') retornam False
if True and 0 and True:
    print("verdadeiro")
else:
    print("Falso")

if True or False:
    print("Condição verdadeira")
else:
    print("Falso")
