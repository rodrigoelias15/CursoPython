# is e not is (comparadores)

variavel = None
num = input("Digite um valor: ")

if type(num) is type(str()):
    num = float(num)
    print(f"Valor {num} do tipo str foi convertido para tipo {type(num)}")
else:
    print("Não eh do tipo str")

if variavel is None:
    variavel = 10
    print(f"Valor da variável atualizado para {variavel}")
else:
    print(f"Variável mantem valor como {variavel}")

print(f"Variavel é 'None'?", variavel is None)