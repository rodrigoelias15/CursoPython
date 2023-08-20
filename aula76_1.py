"""
Dicionarios
"""

import copy

pessoa = {
    "nome": "Rodrigo",
    "idade": 32,
    "etnia": "negra",
    "endereco": [
        {"bairro": "Bairu", "rua": "Maurício Duarte"},
        {"bairro": "Progresso", "rua": "Angelino Maurilio"},
    ]
}

print("Tipo do \"dicionario\":", type(pessoa))

print("Bairro:", pessoa["endereco"][0]["bairro"])

print(pessoa)

del pessoa["etnia"]

print(pessoa)

chave = "nome1"

# método "get()" do dicionário retorna valor da chave, caso a chave não exista, retorna "None"
if pessoa.get(chave) is None:
    print(pessoa.get(chave))
else:
    print(pessoa[chave])
    
pessoa.pop("nome") # deleta chave especificada

print(pessoa.keys()) # lista as chaves do dicionario

print(pessoa.values()) # lista os valores do dicionario

dicionario1 = {
    "nome": "Rodrigo",
    "idade": 32,
}

dicionario2 = dicionario1 # dicionario2 aponta para mesmo local de memória do dicionario1, portanto se dicionario1 for alterado depois, dicionario2 também é alterado

dicionario1["idade"] = 45

print(f"Endereço de \"dicionario1\":", hex(id(dicionario1))) # metodo id() retorna endereço de memória do objeto e hex() converte para hexadecimal

print(f"Endereço de \"dicionario2\":", hex(id(dicionario2)))

print("dicionario1 alterado, alterando dicionario2 simultaneamente:", dicionario2)

dicionario2 = copy.copy(dicionario1) # para ser feito uma copia profunda (com indices mais internos, como listas e tuplas), podemos usar o módulo "copy" e chamar o método "copy()", desta forma um dicionário não mais afetará o outro

dicionario1["idade"] = 70

print("dicionario1:", dicionario1)

print("Copia profunda de dicionario1, dicionario2 não é afetado:", dicionario2)

print(f"Endereço de \"dicionario1\":", hex(id(dicionario1)))

print(f"Endereço de \"dicionario2\":", hex(id(dicionario2)))

dicionario1.update({
    "idade": 50, # altera valor existente
    "altura": 1.7 # se chave não existir, cria uma nova
})

print("dicionario1:", dicionario1)

dicionario1.popitem() # apaga ultima chave

print("dicionario1:", dicionario1)