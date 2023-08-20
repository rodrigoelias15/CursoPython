condicao = True
nome = "Rodrigo"

while condicao:
    nome = input(f"Digite nome: ")
    if nome == "Rodrigo":
        break
    else:
        print("Erro")
    
print("saiu do For")
