nome = "Rodrigo"
i = 0
novo_nome = ''

while i < len(nome):
    letra = nome[i]
    novo_nome += "*" + letra
    i+=1
    
novo_nome += "*"

print(novo_nome)