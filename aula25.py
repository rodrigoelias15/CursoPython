# Exemplos de formatação com f-strings

# > - esquerda
# < - direita
# ^ - centro

variavel = "ABC"

print(f"{variavel:_>10} FIM") # adiciona 10 caracteres "_" à esquesta de "variavel"
print(f"{variavel:_<10} FIM") # adiciona 10 caracteres "_" à direita de "variavel"
print(f"{variavel:_^10} FIM") # adiciona 10 caracteres "_" ao centro de "variavel"