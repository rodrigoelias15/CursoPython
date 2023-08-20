"""
Clousure pt2
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!!"
    return saudar # corpo da função "saudar" não é executado

diz_bom_dia = criar_saudacao("Bom dia")
diz_ola = criar_saudacao("Olá")

print(diz_bom_dia("Rodrigo")) # "resolve" a função criar_saudacao(saudacao) e adia a passagem do argumento "nome"
print(diz_ola("Mateus"))

for nome in ["rodrigo", "mateus", "juarez"]:
    print(diz_bom_dia(nome))
    print(diz_ola(nome))