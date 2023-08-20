
""" Teste de conhecimento da aula 1 até 30 """

print(r"Esta mensagem é só para teste, você verá que pode ver todos caracteres (inclusive backslashs) por conta do \"r\" no início da string, ele serve para expressões regulares no python")
print() # por terminar em \n, um print() vazio solta uma linha

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
idade = int(idade)
nome_completo = nome + " " + sobrenome
print("Seu nome", nome_completo, sep=": ", end=" ") # parâmetro "end" altera padrão do print() que é "\n"
print("Idade", idade, sep=": ") # separador alterado, padrão "sep" é um espaço

variavel = input("Digite um número inteiro diferente de '0', ele será armazenado como string: ")

if (variavel.isdigit() and not variavel == "0") or (variavel.isdigit() and variavel != "0"):
    variavel = float(variavel)
    print(f"Vc digitou corretamente, {variavel:.2f} foi convertido para float")
    denominador = input(f"Digite um número diferente de 0 para dividir o {variavel:.2f}: ")
    denominador = float(denominador)
    try:
        RESULTADO = variavel/denominador
        print(f"Resultado é uma CONSTANTE do tipo {type(RESULTADO)} e vale: {variavel/denominador:.2f}")
        print(f"Número foi completado com 0's à esquerda para que se tenha 8 dígitos: {RESULTADO:0>8}")
        if RESULTADO % 2 == 0:
            print(f"{RESULTADO} é par e o cubo dele é {RESULTADO**3}")
        else:
            print(f"{RESULTADO} é ímpar e o cubo dele é {RESULTADO**3}")
    except:
        print(f"Erro na divisão, não podemos dividir por {denominador}")
else:
    print(f"\"{variavel}\" ou não é inteiro ou é igual a \"0\"")

print(f"Seu nome completo tem {len(nome_completo)} caracteres e de trás pra frente é \"{nome_completo[::-1]}\", sendo que a primeira letra é {nome_completo[0]} e última letra é {nome_completo[-1]}")

print("Seu nome completo possui vogal 'a'?", "a" in nome_completo)