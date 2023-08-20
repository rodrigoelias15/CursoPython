"""
Tuplas são o mesmo que listas, porém são imutáveis
"""

tupla = ("rodrigo", "maria", "joao") # tuplas podem ser  representadas por parênteses ou não receberem colchetes
# tupla = list(tupla) # converte tupla para tipo "lista" (neste caso, qualquer item pode ser modificado)
# tupla = tuple(tupla) # converte variável para tipo "tupla"

for indice, nome in enumerate(tupla): # enumerate() exibe índices da lista/tupla, neste caso usando desempacotamento
    print(indice, nome)

try:
    tupla[1] = "hueheuhe"
    print(tupla)
except:
    print("ERRO! Tupla é um tipo imutável")
