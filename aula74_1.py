"""
Clousure pt1
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}!!"
    return saudar # corpo da função "saudar" não é executado

s1 = criar_saudacao("Bom dia", "Rodrigo")
s2 = criar_saudacao("Olá", "Mateus")

print(s1()) # "resolve" a função criar_saudacao(saudacao, nome)
print(s2())