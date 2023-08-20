nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome[::1]}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print("Contém espaço")
    else:
        print("Não Contém espaço")

    tamanho_nome = len(nome)

    print(f"Seu nome tem {tamanho_nome} letras")
    print(f"A primeira letra do Seu nome é {nome[0]}")
    print(f"A ultima letra do Seu nome é {nome[-1]}")
    # print(f"A ultima letra do Seu nome é {nome[tamanho_nome - 1]}")
else:
    print("Desculpe, você deixou campos vazios!")
    
