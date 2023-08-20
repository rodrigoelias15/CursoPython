# try/except
# Diferente de if/else, try/except trabalha com erros de código

str = input("Digite uma letra ou número: ")

try:
    letra_ou_numero = float(str) # se digitar letra, vai gerar erro porque nenhuma letra pode ser convertida para float
    print(letra_ou_numero)
except:
    print("Código gerou erro na conversão")
