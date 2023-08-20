# condições if, elif e else

if input("Seu nome: ") == "Rodrigo":
    print("Nome correto")
elif input("Digite nome novamente: ") == "rodrigo":
    print("Nome correto, porém digite com \"R\" maiúsculo na próxima")
else:
    print("Nome errado")


if 10 <= 5:
    print("Proposição correta!")
else:
    pass # ou ellipsis "..."