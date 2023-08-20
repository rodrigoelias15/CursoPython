"""
    Empacotamento e Desempacotamento
"""

lista = ["rodrigo", "maria", "joao"]

nome1, nome2, nome3 = ["rodrigo", "maria", "joao"] # desempacotamento

print(nome1, nome2, nome3)

nome1, *_ = ["rodrigo", "maria", "joao"] # "*" significa que vai pegar o restante dos elementos iteráveis

print(nome1, _) # "_" é uma convenção, significa que é uma variável que não será usada

item1, item2, item3 = 12, 50, 80

print(item2)

num1, num2, *num = 5, 20, 30, 40, 18, 79 # Empacotamento em *num. *num gera uma tupla

print(num1, num2, *num)