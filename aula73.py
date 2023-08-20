
def bom_dia(msg1, msg2):
    return f"{msg1} {msg2}"

def retorna_msg(funcao, *args): # função de primeira classe, higher order function ou função de ordem superior (função que retorna outra função)
    return funcao(*args) # função recebe mesma qtd de argumentos da função que será chamada no argumento da função de primeira classe (higher order function)

print(retorna_msg(bom_dia, "boa noite", "bom dia"))