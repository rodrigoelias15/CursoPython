"""
Definição de funções
Parâmetros são as "variáveis" passadas nas funções, argumentos são os valores (conteúdos) passados
Funções retornam "None" por padrão
Funções podem ser definidas (def) dentro do escopo de outras
"""

var = 40

def soma(x, y):
    print(f"Soma de {x} e {y}:", x + y)
    global var # altera escopo da variavel
    var = 13 # a função passa a alterar a variável declarada em escopo global
    
soma(2,1) # argumentos não nomeados (ou posicionais)

soma(y=2, x=1) # argumentos nomeados (parâmetros)

soma(2, y=1) # argumentos nomeados podem ser escritos após argumentos não nomeados (posicionais), contanto que não sejam passados mais de um argumento para cada parâmetro

print(soma(2,1))

print(var)