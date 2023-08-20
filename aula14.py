""" formatação de strings """

nome = "Rodrigo"
idade = "32"

# Primeira forma de formatar string
str1 = f"{nome} está com {idade} anos"

# Segunda forma de formatar
str2 = "{} está com {} anos"
string_formatada2 = str2.format(nome, idade)

# Terceira forma de formatar
str3 = "{0} está com {1} anos"
string_formatada3 = str3.format(nome, idade)

# Quarta forma de formatar
str4 = "{nomeParam} está com {idadeParam} anos"
string_formatada4 = str4.format(nomeParam = nome, idadeParam = idade) # format(parametro1 = argumento1, ....)

print(str1)
print(string_formatada2)
print(string_formatada3)
print(string_formatada4)

conta1 = 1 + 3.4
conta2 = 1 * 3.4

print(conta1)
print(conta2)