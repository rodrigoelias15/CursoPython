# fatiamento de strings

# inicio (inicio do intervalo) : fim (fim do intervalo): passo (de quantos em quantos indices vai iterar (incremento))
# [i:f:p]
# i : f significa i < f, ou seja, letra que está no índice "f" não conta

str = "Rodrigo"
print("Fatiamento com menos parâmetros (1):", str[:3]) # mesmo que str[0:3:1]
print("Fatiamento com menos parâmetros (2):", str[3:]) # mesmo que str[3::1]

print(str[0:4:3])

print(str[::1]) # início e fim vazios significa que vai pegar no primeiro caracter até o último

print(str[::-1]) # imprime string de trás pra frente, último índice da string é -1 e é decrescido quando percorrido de trás para frente

print(len(str[0:4:3]))
print("Comprimento total da string:", len(str))