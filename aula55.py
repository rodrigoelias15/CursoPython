# Arredondamento de números de ponto flutuante

import decimal as dc

numero = 54.666

print(round(numero,2)) # arredondamento
print(dc.Decimal(numero)) # modulo do python que aproveita o máximo de casas decimais