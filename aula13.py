nome = "Rodrigo"
altura = 1.7
peso = 67
imc = ... # ellipsis ou "trẽs pontinhos" significa que o código ainda não foi escrito, mas pode ser escrito depois, não gerando erro de código)

imc = peso/(altura ** 2) # ou peso/altura ** 2, potencia ou exponenciação tem precedência maior que outros operadores, parênteses tem maior precedência de todos

# Formatação de strings
# f-strings: basta acrescentar um "f" colado e antes da string, e colocar variáveis entre chaves. Obs: Dentro das chaves podemos realizar operações também

print(f"{nome} tem {altura} de altura e possui {peso} quilos, seu imc é de {imc:.2f}")

# ou

string1 = f"{nome} tem {altura} de altura e possui {peso} quilos, seu imc é de {imc:.2f}"

print(string1)