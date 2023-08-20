nome = "Rodrigo"
altura = 1.7
peso = 67
imc = ... # ellipsis ou "trẽs pontinhos" significa que o código ainda não foi escrito, mas pode ser escrito depois, não gerando erro de código)

imc = peso/(altura ** 2) # ou peso/altura ** 2, potencia ou exponenciação tem precedência maior que outros operadores, parênteses tem maior precedência de todos

print(nome, "tem", altura, "de altura")
print("pesa", peso, "quilos e seu imc é", imc)